// TenantFlex background check (Android app, no Firebase or other push service).
// Android runs this about every 15 minutes, even while the app is closed: it asks the TenantFlex server for
// notifications newer than the last one seen and shows them as system notifications.
// The app tells it which server and account to use ('configure') and what it has already shown ('seen').
// Runs in Capacitor's Background Runner: no DOM or modules, state kept in CapacitorKV.

function get(key) {
  const r = CapacitorKV.get(key);
  return r && r.value ? r.value : '';
}

addEventListener('configure', (resolve, reject, args) => {
  try {
    if (args && args.token) {
      CapacitorKV.set('server', String(args.server || ''));
      CapacitorKV.set('token', String(args.token));
      if (args.lastId != null && Number(args.lastId) > Number(get('lastId') || 0)) CapacitorKV.set('lastId', String(args.lastId));
    } else {
      CapacitorKV.remove('token'); // signed out or notifications turned off
    }
    resolve();
  } catch (err) {
    reject(err);
  }
});

addEventListener('seen', (resolve, reject, args) => {
  try {
    if (args && Number(args.lastId) > Number(get('lastId') || 0)) CapacitorKV.set('lastId', String(args.lastId));
    resolve();
  } catch (err) {
    reject(err);
  }
});

addEventListener('check', async (resolve, reject) => {
  try {
    const token = get('token');
    if (!token) return resolve();
    const lastId = Number(get('lastId') || 0);
    const res = await fetch(`${get('server')}/api/notifications?after=${lastId}`, { headers: { authorization: `Bearer ${token}` } });
    if (res.status === 401) { CapacitorKV.remove('token'); return resolve(); }
    if (!res.ok) return resolve();
    const { items } = await res.json();
    // Newest few unread ones only, oldest first, so a long absence doesn't flood the phone.
    const fresh = items.filter((n) => !n.read_at).sort((a, b) => a.id - b.id).slice(-5);
    if (fresh.length) {
      CapacitorNotifications.schedule(fresh.map((n) => ({
        id: n.id % 2147483647, title: n.title, body: n.body || '', largeBody: n.body || '',
        channelId: 'tenantflex', smallIcon: 'ic_stat_tenantflex', autoCancel: true, extra: { notification_id: String(n.id) },
      })));
    }
    const newest = items.reduce((m, n) => Math.max(m, n.id), lastId);
    if (newest > lastId) CapacitorKV.set('lastId', String(newest));
    resolve();
  } catch (err) {
    reject(err);
  }
});
