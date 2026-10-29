// TenantFlex service worker: shows push notifications when the web app is closed or in the background,
// and opens the right screen when one is tapped. (No offline caching: the app always loads fresh.)
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => event.waitUntil(self.clients.claim()));

self.addEventListener('push', (event) => {
  let n;
  try { n = event.data.json(); } catch { n = { title: 'TenantFlex', body: event.data ? event.data.text() : '' }; }
  event.waitUntil((async () => {
    // If the app is open on screen it shows the notification itself (no duplicate system banner).
    const windows = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    const visible = windows.find((w) => w.visibilityState === 'visible');
    if (visible) { visible.postMessage({ type: 'push', notification: n }); return; }
    const app = n.app === 'manager' ? 'manager' : 'tenant';
    await self.registration.showNotification(n.title || 'TenantFlex', {
      body: n.body || '',
      icon: `./icons/${app}-192.png`,
      badge: `./icons/${app}-192.png`,
      tag: n.data && n.data.notification_id ? `tf-${n.data.notification_id}` : undefined,
      data: n.data || {},
    });
  })());
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const id = (event.notification.data && event.notification.data.notification_id) || '';
  event.waitUntil((async () => {
    const windows = await self.clients.matchAll({ type: 'window', includeUncontrolled: true });
    if (windows.length) {
      const w = windows[0];
      await w.focus();
      w.postMessage({ type: 'open-notification', id });
      return;
    }
    await self.clients.openWindow(`./?notification=${encodeURIComponent(id)}`);
  })());
});
