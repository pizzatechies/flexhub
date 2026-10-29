# Builds the static TenantFlex website (HTML pages at the repository root). Run: python3 tools/build_site.py
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
import legal_content as legal
I = lambda n, cls='': f'<svg class="{cls}" aria-hidden="true"><use href="assets/img/icons.svg#{n}"/></svg>'

def page(name, title, desc, body):
    nav = [('index.html', 'Home'), ('index.html#tenants', 'Tenant app'), ('index.html#management', 'Manager app'),
           ('index.html#payments', 'Payments'), ('features.html', 'Features'), ('pricing.html', 'Pricing'), ('demo.html', 'Live demo'), ('contact.html', 'Contact')]
    links = '\n'.join(f'<a href="{h}"{" class=\"on\"" if h == name else ""}>{t}</a>' for h, t in nav)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#000000">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/og-card.jpg">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/img/icon-192.png">
<link rel="apple-touch-icon" href="assets/img/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/img/logo.png" alt=""><span class="gold-text">TENANTFLEX</span></a>
    <button class="menu-btn" aria-label="Menu">{I('menu')}</button>
    <nav class="nav-links">
      {links}
      <a class="btn gold sm" href="contact.html">Contact us</a>
    </nav>
  </div>
</header>
<main>
{body}
</main>
<footer>
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/img/logo.png" alt="" style="width:34px;height:34px"><span class="gold-text" style="font-size:16px">TENANTFLEX</span></a>
    <nav><a href="index.html#how">How it works</a><a href="features.html">Features</a><a href="pricing.html">Pricing</a><a href="demo.html">Live demo</a><a href="index.html#faq">FAQ</a><a href="contact.html">Contact</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp +254 747 354 677</a><a href="{EMAIL}">info@pizzatechnologies.co.ke</a></nav>
    <nav class="legal-links"><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="data-processing.html">Data Processing Terms</a><a href="delete-account.html">Delete your account</a></nav>
    <div>© <span id="year">2026</span> TenantFlex · by Pizza Technologies</div>
  </div>
</footer>
<script src="assets/js/site.js"></script>
</body>
</html>
'''

WA = 'https://wa.me/254747354677?text=' + 'Hello%20Pizza%20Technologies%2C%20I%27d%20like%20to%20get%20TenantFlex%20for%20my%20complex.'
EMAIL = 'mailto:info@pizzatechnologies.co.ke?subject=TenantFlex%20enquiry'
contact_btns = lambda center=False: f'<div class="btns"{" style=\"justify-content:center\"" if center else ""}><a class="btn gold" href="{WA}" target="_blank" rel="noopener">{I("whatsapp")} WhatsApp +254 747 354 677</a><a class="btn outline" href="{EMAIL}">{I("mail")} info@pizzatechnologies.co.ke</a></div>'
# ---- Subscription rates paid by complex management (KES). Change prices here only.
PLANS = [
  dict(name='Starter', units='Up to 20 units', monthly=5000, annual=50000, featured=False,
       blurb='For small plazas, markets and office blocks.',
       items=['TenantFlex + TenantFlex Manager on web, Windows, Android &amp; iOS', 'M-Pesa, Airtel Money, T-Kash, card &amp; bank transfer', 'Instant receipts, rent &amp; utility billing', 'Messaging, notices &amp; reminders', '1 manager account', 'WhatsApp &amp; email support']),
  dict(name='Business', units='Up to 75 units', monthly=15000, annual=150000, featured=True,
       blurb='For busy malls and business complexes.',
       items=['Everything in Starter', 'Up to 5 manager accounts', 'Meter-reading billing for all units', 'Bank-transfer confirmation queue', 'Onboarding &amp; training session', 'Priority WhatsApp support']),
  dict(name='Enterprise', units='Unlimited units', monthly=30000, annual=300000, featured=False,
       blurb='For property groups running several complexes.',
       items=['Everything in Business', 'Multiple complexes', 'Unlimited manager accounts', 'Help connecting your M-Pesa / bank gateway', 'On-site training', 'Dedicated account manager']),
]
kes = lambda n: f'KES {n:,.0f}'

def pricing_section(head_tag='h2'):
    cards = []
    for pl in PLANS:
        wa_m = WA.split('?')[0] + '?text=' + (f'Hello%20Pizza%20Technologies%2C%20I%27d%20like%20the%20TenantFlex%20{pl["name"]}%20plan%20(monthly).')
        wa_a = WA.split('?')[0] + '?text=' + (f'Hello%20Pizza%20Technologies%2C%20I%27d%20like%20the%20TenantFlex%20{pl["name"]}%20plan%20(annual).')
        items = ''.join(f'<li>{i}</li>' for i in pl['items'])
        cards.append(f'''
      <div class="plan{' featured' if pl['featured'] else ''} reveal">
        {'<span class="plan-badge">Most popular</span>' if pl['featured'] else ''}
        <h3>{pl['name']}</h3>
        <p class="muted plan-blurb">{pl['blurb']}</p>
        <div class="plan-units">{pl['units']}</div>
        <div class="plan-price" data-monthly="{kes(pl['monthly'])}" data-annual="{kes(pl['annual'])}">{kes(pl['monthly'])}</div>
        <div class="plan-per" data-monthly="per month, billed monthly" data-annual="per year, about {kes(round(pl['annual'] / 12))} a month">per month, billed monthly</div>
        <ul class="checks plan-items">{items}</ul>
        <a class="btn {'gold' if pl['featured'] else 'outline'} plan-cta" href="{wa_m}" data-monthly="{wa_m}" data-annual="{wa_a}" target="_blank" rel="noopener">{I('whatsapp')} Get {pl['name']}</a>
      </div>''')
    return f'''
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Pricing</span>
      <{head_tag}>Simple rates for complex management</{head_tag}>
      <p class="lead">One subscription per complex, paid by management. Tenants use TenantFlex free. Pay monthly, or pay annually and get <b style="color:var(--gold-light)">2 months free</b>.</p>
      <div class="billing-toggle" role="group" aria-label="Billing period">
        <button type="button" class="on" data-period="monthly">Monthly</button>
        <button type="button" data-period="annual">Annual <span class="save">2 months free</span></button>
      </div>
    </div>
    <div class="plans">{''.join(cards)}
    </div>
    <p class="muted plan-note reveal">All prices are in Kenyan Shillings (KES). Mobile-money and card transaction fees are charged by the payment provider. Need something different? <a href="contact.html">Contact us</a> for a custom quote.</p>
  </div>'''

phone = lambda img, alt: f'<div class="phone"><img class="zoom" src="assets/img/{img}.jpg" alt="{alt}" loading="lazy"></div>'
browser = lambda img, alt, url='tenantflex · manage': f'<div class="browser"><div class="bar"><i></i><i></i><i></i><span>{url}</span></div><img class="zoom" src="assets/img/{img}.jpg" alt="{alt}" loading="lazy"></div>'
def checks(items): return '<ul class="checks">' + ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in items) + '</ul>'

# ---------------------------------------------------------------- index
index = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <span class="eyebrow">Tenancy · Billing · Payments</span>
      <h1>Every bill. Every payment. <span class="gold-text">One place.</span></h1>
      <p class="lead">TenantFlex connects business and shopping complexes with their tenants. Tenants see every charge and pay rent, electricity and water right in the app. Management bills, collects, issues receipts and talks to tenants in one system.</p>
      <div class="btns">
        <a class="btn gold" href="demo.html">{I('dashboard')} Try the live demo</a>
        <a class="btn outline" href="contact.html">{I('whatsapp')} Contact us</a>
      </div>
      <div class="hero-tags">
        <span class="tag"><b>M-Pesa</b> · Airtel Money · T-Kash · Card · Bank</span>
        <span class="tag">Kenyan Shilling <b>(KES)</b> by default</span>
        <span class="tag"><b>Web</b> · Windows · Android · iOS</span>
      </div>
    </div>
    <div class="hero-visual">
      {browser('manager-dashboard', 'TenantFlex Manager dashboard')}
      {phone('tenant-home', 'TenantFlex tenant home screen with payments due')}
    </div>
  </div>
</section>

<div class="facts">
  <div class="wrap">
    <div class="fact"><b class="gold-text">2 apps</b><span>One for tenants, one for complex management</span></div>
    <div class="fact"><b class="gold-text">5 ways</b><span>to pay in the app, plus cash at the office</span></div>
    <div class="fact"><b class="gold-text">Instant</b><span>receipts the moment a payment completes</span></div>
    <div class="fact"><b class="gold-text">Any complex</b><span>malls, plazas, office parks and markets</span></div>
  </div>
</div>

<section id="how">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">How it works</span>
      <h2>From sign-up to paid in four steps</h2>
      <p class="lead">TenantFlex works for any number of complexes. Each one gets its own tenants, rates, bank details and invite code.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>Register your complex</h3><p>Management signs up in TenantFlex Manager, then sets the currency, billing day, electricity and water rates, and bank account.</p></div>
      <div class="step reveal"><h3>Add units &amp; tenants</h3><p>Add your shops, offices and stalls. Tenants join with your invite code, or you create their accounts and assign units.</p></div>
      <div class="step reveal"><h3>Bill automatically</h3><p>Rent is billed on your billing day, meter readings become electricity and water bills, and one-off charges go out in seconds. Tenants are prompted instantly.</p></div>
      <div class="step reveal"><h3>Get paid &amp; receipted</h3><p>Tenants pay in the app and receive a receipt immediately. Bank transfers wait for you to confirm, and cash is receipted at the office.</p></div>
    </div>
  </div>
</section>

<section id="tenants" style="background:var(--bg-2)">
  <div class="wrap split">
    <div class="split-text reveal">
      <span class="eyebrow">TenantFlex · for tenants</span>
      <h2>Your rent, utilities and receipts, all in your pocket</h2>
      <p class="lead">Tenants always know what they owe and why, and can settle it in a few taps.</p>
      {checks([
        ('Every bill and new charge:', 'rent, electricity, water, service charges and penalties, with meter readings and rates shown.'),
        ('Payment prompts:', 'overdue bills and anything due within 7 days appear on the home screen with a Pay button.'),
        ('Pay in the app:', 'M-Pesa, Airtel Money, T-Kash, debit/credit card or bank transfer. Pay everything at once, or part of a bill.'),
        ('Instant receipts:', 'generated the moment a payment completes, then saved, downloadable as PDF and shareable.'),
        ('Talk to management:', 'chat about bills or repairs, and read notices from the complex.'),
      ])}
      <div class="btns" style="margin-top:8px"><a class="btn gold" href="demo/tenant/">{I('phone')} Try the tenant app live {I('arrow')}</a></div>
      <p class="muted" style="font-size:14px">Pay a bill with M-Pesa, get the receipt, and chat with management. Works best on your phone.</p>
    </div>
    <div class="phones reveal">
      {phone('tenant-pay-method', 'Choosing M-Pesa to pay')}
      {phone('tenant-home', 'Tenant home with payment prompts')}
    </div>
  </div>
</section>

<section id="management">
  <div class="wrap split reverse">
    <div class="split-text reveal">
      <span class="eyebrow">TenantFlex Manager · for management</span>
      <h2>Run the whole complex from one dashboard</h2>
      <p class="lead">See what's collected, what's outstanding and who's overdue, then act on it straight away.</p>
      {checks([
        ('Live dashboard:', 'collections this month, outstanding and overdue balances, occupancy, six-month trend and top debtors.'),
        ('Tenants &amp; units:', 'invite codes, tenant statements, unit assignments, rent and meter readings.'),
        ('Billing:', 'monthly rent runs, meter readings that turn into utility bills automatically, and one-off charges to one tenant or everyone.'),
        ('Payments:', 'every payment as it happens. Confirm bank transfers, and record cash or cheques with instant receipts.'),
        ('Communication:', 'a message inbox for every tenant, and notices that reach every tenant at once.'),
      ])}
      <div class="btns" style="margin-top:8px"><a class="btn gold" href="demo/manager/">{I('dashboard')} Open the management demo {I('arrow')}</a></div>
      <p class="muted" style="font-size:14px">The real TenantFlex Manager running in your browser with a sample complex. No sign-up needed.</p>
    </div>
    <div class="reveal">{browser('manager-payments', 'Payments with bank transfers to confirm')}</div>
  </div>
</section>

<section id="payments" style="padding-top:40px">
  <div class="wrap">
    <div class="panel reveal">
      <div class="split">
        <div class="split-text">
          <span class="eyebrow">Payments &amp; receipts</span>
          <h2>Pay the way Kenya pays</h2>
          <p class="lead">Tenants choose how to pay, and each payment goes straight against their bills, oldest first.</p>
          <div class="methods">
            <span class="method">{I('phone')} M-Pesa</span><span class="method">{I('phone')} Airtel Money</span><span class="method">{I('phone')} T-Kash</span>
            <span class="method">{I('card')} Debit / credit card</span><span class="method">{I('bank')} Bank transfer</span><span class="method">{I('cash')} Cash at the office</span>
          </div>
          {checks([
            ('Mobile money &amp; card:', 'the tenant approves the prompt on their phone, and the receipt appears as soon as the payment is confirmed.'),
            ('Bank transfer:', 'the tenant sees your bank details and a reference, then submits their bank transaction code. You confirm it once it reaches the account, and the receipt is issued instantly.'),
            ('Receipts that look the part:', 'numbered per complex (RCT-001-2026-00042), itemised per bill, showing the remaining balance, as a PDF.'),
          ])}
        </div>
        <div class="phones">
          {phone('tenant-bank', 'Bank transfer details')}
          {phone('tenant-receipt', 'Instant payment receipt')}
        </div>
      </div>
    </div>
  </div>
</section>

<section id="billing">
  <div class="wrap split">
    <div class="split-text reveal">
      <span class="eyebrow">Billing automation</span>
      <h2>Bills that send themselves</h2>
      <p class="lead">Spend less time chasing money and more time running the complex.</p>
      {checks([
        ('Automatic monthly rent:', 'every occupied unit is billed on your billing day, and never twice for the same month.'),
        ('Meter readings → utility bills:', 'enter this month\'s electricity or water readings and TenantFlex works out (current − previous) × rate for every unit.'),
        ('One-off charges:', 'service charges, penalties and repairs, sent to one tenant or to every tenant at once.'),
        ('Reminders:', 'tenants are reminded 3 days before a bill is due, and every week while it\'s overdue.'),
      ])}
    </div>
    <div class="reveal">{browser('manager-meters', 'Meter readings turned into electricity bills')}</div>
  </div>
</section>

<section id="communication" style="background:var(--bg-2)">
  <div class="wrap split reverse">
    <div class="split-text reveal">
      <span class="eyebrow">Communication</span>
      <h2>Talk to tenants where they pay</h2>
      <p class="lead">No more scattered calls and texts. Every conversation sits next to the tenant's account.</p>
      {checks([
        ('Direct messages:', 'repairs, questions and complaints, with read receipts.'),
        ('Notices:', 'parking closures, water interruptions and meetings, sent to every tenant\'s app at once.'),
        ('Notifications:', 'new bills, due dates, overdue reminders, receipts and replies, in the app and on the device.'),
      ])}
    </div>
    <div class="phones reveal">
      {phone('tenant-chat', 'Tenant chatting with management')}
      {phone('manager-phone', 'Manager app on a phone')}
    </div>
  </div>
</section>

<section id="features">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Everything included</span>
      <h2>Built for complexes of every size</h2>
    </div>
    <div class="cards">
      <div class="card reveal"><div class="ic">{I('bell')}</div><h3>Payment prompts</h3><p>Rent, electricity and water prompts on the tenant's home screen, plus notifications for every new bill.</p></div>
      <div class="card reveal"><div class="ic">{I('receipt')}</div><h3>Instant receipts</h3><p>Numbered, itemised PDF receipts the moment a payment completes, for both tenant and management.</p></div>
      <div class="card reveal"><div class="ic">{I('bank')}</div><h3>Bank transfer confirmation</h3><p>Transfers queue for management to confirm. Bills are held so nobody pays twice.</p></div>
      <div class="card reveal"><div class="ic">{I('bolt')}</div><h3>Meter-reading billing</h3><p>Electricity and water bills worked out per unit from your readings and rates.</p></div>
      <div class="card reveal"><div class="ic">{I('key')}</div><h3>Automatic rent</h3><p>Every occupied unit billed on your billing day, with your payment terms.</p></div>
      <div class="card reveal"><div class="ic">{I('chart')}</div><h3>Dashboard &amp; statements</h3><p>Collections, arrears, occupancy and a full statement for every tenant.</p></div>
      <div class="card reveal"><div class="ic">{I('chat')}</div><h3>Messaging</h3><p>One conversation per tenant, visible to the whole management team.</p></div>
      <div class="card reveal"><div class="ic">{I('megaphone')}</div><h3>Notices</h3><p>Announcements delivered to every tenant's app with one click.</p></div>
      <div class="card reveal"><div class="ic">{I('cash')}</div><h3>Office payments</h3><p>Record cash, cheques and bank deposits, receipted on the spot.</p></div>
      <div class="card reveal"><div class="ic">{I('building')}</div><h3>For any business</h3><p>Malls, plazas, office parks and markets, each with its own invite code, currency and rates.</p></div>
      <div class="card reveal"><div class="ic">{I('users')}</div><h3>Team access</h3><p>Add more managers. Everyone sees the same live data.</p></div>
      <div class="card reveal"><div class="ic">{I('shield')}</div><h3>Secure by design</h3><p>PostgreSQL with row-level locking for payments, hashed passwords, and data scoped to each complex.</p></div>
    </div>
    <div class="btns" style="justify-content:center;margin-top:36px"><a class="btn outline" href="features.html">See every screen {I('arrow')}</a></div>
  </div>
</section>

<section id="platforms" style="background:var(--bg-2)">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">Everywhere your tenants are</span>
      <h2>One system, every device</h2>
      <p class="lead">Both apps run in the browser, on Windows PCs and on Android and iOS phones, each opening with the same black-and-gold splash screen. We install and set them up for your complex.</p>
    </div>
    <div class="app-icons reveal">
      <figure><img class="app-icon lg" src="assets/img/app-tenant.png" alt="TenantFlex app icon"><figcaption>TenantFlex<span>for tenants</span></figcaption></figure>
      <figure><img class="app-icon lg" src="assets/img/app-manager.png" alt="TenantFlex Manager app icon"><figcaption>TenantFlex Manager<span>for management</span></figcaption></figure>
    </div>
    <div class="platforms reveal">
      <div class="platform">{I('globe')}<b>Web</b><span>Any browser</span></div>
      <div class="platform">{I('windows')}<b>Windows</b><span>Installer &amp; portable .exe</span></div>
      <div class="platform">{I('android')}<b>Android</b><span>.apk</span></div>
      <div class="platform">{I('apple')}<b>iOS</b><span>iPhone &amp; iPad</span></div>
      <div class="platform">{I('server')}<b>Server</b><span>Your PC, office server or cloud</span></div>
    </div>
  </div>
</section>

<section id="demo" style="padding:20px 0 0">
  <div class="wrap">
    <div class="panel reveal split" style="gap:40px">
      <div class="split-text">
        <span class="eyebrow">Live demo</span>
        <h2>Try both apps now</h2>
        <p class="lead">Explore TenantFlex with the Golden Gate Plaza sample complex. As management, confirm a bank transfer, record cash or bill meter readings. As a tenant, pay a bill with M-Pesa and get your receipt instantly. Everything runs in your browser, and nothing is saved.</p>
        <div class="btns"><a class="btn gold" href="demo/manager/">{I('dashboard')} Management demo</a><a class="btn gold" href="demo/tenant/">{I('phone')} Tenant demo</a><a class="btn outline" href="contact.html">Book a guided demo</a></div>
      </div>
      <a href="demo/manager/" aria-label="Launch the management demo">{browser('manager-dashboard', 'TenantFlex Manager live demo', 'Live demo · Golden Gate Plaza')}</a>
    </div>
  </div>
</section>

<section id="pricing">{pricing_section()}
</section>

<section id="faq" style="background:var(--bg-2)">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow">FAQ</span><h2>Questions, answered</h2></div>
    <div class="faq reveal">
      <details><summary>Which payment methods can tenants use?</summary><p>M-Pesa, Airtel Money, T-Kash, debit/credit card and bank transfer in the app. Management can also record cash, cheques and bank deposits made at the office, with a receipt issued immediately.</p></details>
      <details><summary>How do live M-Pesa and card payments work?</summary><p>Mobile money and card payments go through a payment-gateway connector. During setup you connect your own merchant account (for example M-Pesa Daraja / STK Push, Airtel Money or a card gateway), and money goes straight to your account. Bank transfers and office payments work without any gateway.</p></details>
      <details><summary>When does a tenant get their receipt?</summary><p>The moment the payment completes: right after the mobile-money or card approval, as soon as management confirms a bank transfer, or immediately for cash recorded at the office. Receipts are saved in the app and can be downloaded as PDF.</p></details>
      <details><summary>Can we use a currency other than Kenyan Shillings?</summary><p>Yes. KES is the default, and each complex can choose its own currency (USD, UGX, TZS, RWF and others) when it registers, or later in Settings.</p></details>
      <details><summary>Can one company run several complexes?</summary><p>Yes. Each complex is registered separately with its own tenants, units, rates, bank account and invite code.</p></details>
      <details><summary>Do tenants have to install an app?</summary><p>No. They can use the web version in any browser, or install the Android, iOS or Windows app. It's the same account on every device.</p></details>
      <details><summary>Who pays for TenantFlex?</summary><p>The complex management pays one subscription per complex, monthly or annually (annual billing gets 2 months free). Tenants download and use the TenantFlex app for free.</p></details>
      <details><summary>Where is our data stored?</summary><p>On your own TenantFlex server, in a PostgreSQL database. That can be an office PC, your own server or a cloud host.</p></details>
    </div>
  </div>
</section>

<section class="cta" style="padding-top:20px">
  <div class="wrap">
    <div class="panel reveal">
      <img src="assets/img/logo.png" alt="">
      <h2>Bring your complex onto <span class="gold-text">TenantFlex</span></h2>
      <p class="lead">Talk to us on WhatsApp or by email. We'll set up TenantFlex for your complex and get your tenants paying in the app.</p>
      {contact_btns(True)}
    </div>
  </div>
</section>
'''
open('index.html','w').write(page('index.html', 'TenantFlex: tenancy, billing & payments for business complexes',
  'Tenants pay rent, electricity and water in the app and get instant receipts. Management bills, collects and communicates in one system.', index))

# ---------------------------------------------------------------- features
def fig(img, title, text, kind='phone'):
    inner = phone(img, title) if kind == 'phone' else browser(img, title)
    return f'<figure class="reveal">{inner}<figcaption><b>{title}</b>{text}</figcaption></figure>'

features = f'''
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Features</span>
    <h1>Every screen, <span class="gold-text">up close</span></h1>
    <p class="lead">These are real screens from the TenantFlex apps, using a demo complex in Nairobi. Tap any screenshot to enlarge it, or try them live: <a href="demo/tenant/">tenant app</a> · <a href="demo/manager/">management app</a>.</p>
  </div>
</section>
<section style="padding-top:20px">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">TenantFlex · tenant app</span><h2>For tenants</h2></div>
    <div class="gallery phones-grid">
      {fig('tenant-splash', 'Splash screen', 'Black and gold, with the logo, every time the app opens.')}
      {fig('tenant-login', 'Sign in or join', 'Tenants join their complex with the invite code from management.')}
      {fig('tenant-home', 'Home & payment prompts', 'Total balance, overdue amount and a Pay button for everything due.')}
      {fig('tenant-bills', 'All bills', 'Rent, utilities and charges, with status and due date.')}
      {fig('tenant-pay-method', 'Choose how to pay', 'M-Pesa, Airtel Money, T-Kash, card or bank transfer.')}
      {fig('tenant-processing', 'Approve on your phone', 'TenantFlex waits for the payment to be confirmed.')}
      {fig('tenant-paid', 'Paid', 'Success screen with the receipt underneath.')}
      {fig('tenant-receipt', 'Instant receipt', 'Numbered and itemised, showing the remaining balance. Download as PDF.')}
      {fig('tenant-bank', 'Bank transfer', 'Bank details and a reference, then the tenant\'s bank transaction code.')}
      {fig('tenant-chat', 'Chat with management', 'Messages go straight to the complex office.')}
    </div>
  </div>
</section>
<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">TenantFlex Manager</span><h2>For management</h2></div>
    <div class="gallery">
      {fig('manager-dashboard', 'Dashboard', 'Collections, arrears, occupancy, six-month trend, top debtors and latest payments.', 'browser')}
      {fig('manager-payments', 'Payments & bank transfers', 'Confirm or reject transfers. The receipt is issued on confirmation.', 'browser')}
      {fig('manager-billing', 'Billing', 'Every bill by status and type. Cancel unpaid bills.', 'browser')}
      {fig('manager-meters', 'Meter readings', 'Electricity and water bills calculated per unit from your readings.', 'browser')}
      {fig('manager-tenants', 'Tenants', 'Balances, overdue amounts, units and unread messages at a glance.', 'browser')}
      {fig('manager-tenant-statement', 'Tenant statement', 'Every bill and payment for one tenant, with quick actions.', 'browser')}
      {fig('manager-messages', 'Messages', 'One conversation per tenant, with read receipts.', 'browser')}
      {fig('manager-notices', 'Notices', 'Announcements delivered to every tenant\'s app.', 'browser')}
      {fig('manager-units', 'Units & spaces', 'Shops, offices and kiosks, with rent, tenant and meter readings.', 'browser')}
      {fig('manager-settings', 'Settings', 'Currency, billing day, payment terms, utility rates, bank account and team.', 'browser')}
    </div>
  </div>
</section>
<section class="cta" style="padding-top:60px">
  <div class="wrap"><div class="panel reveal"><h2>Want TenantFlex for your complex?</h2><p class="lead">Try both apps yourself, or contact us for setup.</p><div class="btns" style="justify-content:center;margin-bottom:12px"><a class="btn gold" href="demo/manager/">{I('dashboard')} Management demo</a><a class="btn gold" href="demo/tenant/">{I('phone')} Tenant demo</a></div>{contact_btns(True)}</div></div>
</section>
'''
open('features.html','w').write(page('features.html', 'Features · TenantFlex', 'Screens from the TenantFlex tenant app and the TenantFlex Manager app.', features))

# ---------------------------------------------------------------- contact
contact = f'''
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Contact us</span>
    <h1>Get <span class="gold-text">TenantFlex</span> for your complex</h1>
    <p class="lead">TenantFlex is set up for each complex by Pizza Technologies. Message us on WhatsApp or send an email and we'll get back to you.</p>
  </div>
</section>
<section style="padding-top:10px">
  <div class="wrap">
    <div class="dl-grid">
      <a class="dl featured reveal" href="{WA}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit">
        <div class="dl-head"><div class="card-ic">{I('whatsapp')}</div><div><h3>WhatsApp</h3><span class="muted">Fastest way to reach us</span></div></div>
        <div class="contact-big gold-text">+254 747 354 677</div>
        <span class="btn gold">{I('whatsapp')} Chat on WhatsApp</span>
      </a>
      <a class="dl reveal" href="{EMAIL}" style="text-decoration:none;color:inherit">
        <div class="dl-head"><div class="card-ic">{I('mail')}</div><div><h3>Email</h3><span class="muted">For quotes, demos and partnerships</span></div></div>
        <div class="contact-big gold-text">info@pizzatechnologies.co.ke</div>
        <span class="btn outline">{I('mail')} Send an email</span>
      </a>
    </div>
  </div>
</section>
<section id="setup" style="background:var(--bg-2)">
  <div class="wrap">
    <div class="section-head"><span class="eyebrow">What happens next</span><h2>From first message to first payment</h2></div>
    <ol class="guide reveal">
      <li><b>Tell us about your complex.</b> The number of units, how you bill rent and utilities today, and how tenants pay.</li>
      <li><b>See a demo.</b> We walk you through TenantFlex and TenantFlex Manager using a sample complex.</li>
      <li><b>We set it up.</b> We set up your TenantFlex server and your payment options (M-Pesa, Airtel Money, T-Kash, card, bank transfer), then install the apps for your management team.</li>
      <li><b>Invite your tenants.</b> Tenants get the TenantFlex app on Android, iPhone, Windows or the web, and join with your complex's invite code.</li>
      <li><b>Start billing.</b> Rent, electricity and water bills go out, tenants pay in the app, and receipts are issued instantly.</li>
    </ol>
  </div>
</section>
'''
open('contact.html','w').write(page('contact.html', 'Contact · TenantFlex', 'Contact Pizza Technologies on WhatsApp (+254 747 354 677) or email (info@pizzatechnologies.co.ke) to get TenantFlex for your complex.', contact))

pricing = f'''
<section class="page-head" style="padding-bottom:0"><div class="wrap"></div></section>
<section style="padding-top:10px">{pricing_section('h1')}
</section>
<section style="background:var(--bg-2)">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow">Pricing FAQ</span><h2>About your subscription</h2></div>
    <div class="faq reveal">
      <details><summary>What's the difference between monthly and annual?</summary><p>Same features. Monthly is billed every month. Annual is paid once a year and costs the same as 10 months, so you get 2 months free.</p></details>
      <details><summary>Do tenants pay anything?</summary><p>No. The subscription is paid by the complex management, and tenants use the TenantFlex app for free.</p></details>
      <details><summary>What if we have more units than our plan allows?</summary><p>Move up to the next plan at any time. Enterprise has no unit limit and covers several complexes.</p></details>
      <details><summary>Are payment-provider fees included?</summary><p>No. M-Pesa, Airtel Money, T-Kash and card transaction fees are charged by the provider under your merchant account. Bank transfers and cash have no TenantFlex fees.</p></details>
      <details><summary>How do we subscribe?</summary><p>Choose a plan and message us on WhatsApp (+254 747 354 677) or email info@pizzatechnologies.co.ke. We'll set up your complex and send the invoice.</p></details>
    </div>
  </div>
</section>
<section class="cta" style="padding-top:60px">
  <div class="wrap"><div class="panel reveal"><h2>Questions about pricing?</h2><p class="lead">We're happy to help you pick the right plan.</p>{contact_btns(True)}</div></div>
</section>
'''
open('pricing.html','w').write(page('pricing.html', 'Pricing · TenantFlex', 'TenantFlex rates for complex management: Starter, Business and Enterprise plans, billed monthly or annually (2 months free).', pricing))

demo_page = f'''
<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Live demo</span>
    <h1>Try <span class="gold-text">TenantFlex</span> live</h1>
    <p class="lead">Both apps run fully in your browser with the Golden Gate Plaza sample complex in Nairobi. There's nothing to install and no sign-up, and nothing you do is saved. Press <b>Reset</b> any time to start again.</p>
  </div>
</section>
<section style="padding-top:10px">
  <div class="wrap">
    <div class="dl-grid">
      <a class="dl featured reveal" href="demo/tenant/" style="text-decoration:none;color:inherit">
        <div class="dl-head"><img class="app-icon" src="assets/img/app-tenant.png" alt="TenantFlex app icon"><div><h3>Tenant app</h3><span class="muted">You are Brian Otieno · Otieno Fashion House · Shop G-01</span></div></div>
        <div class="phone" style="width:220px;align-self:center"><img src="assets/img/tenant-home.jpg" alt="Tenant demo"></div>
        <ul class="checks">
          <li><span><b>Pay your bills</b> with M-Pesa, Airtel Money, T-Kash, card or bank transfer</span></li>
          <li><span><b>Get the receipt</b> the moment the payment completes, and download it as PDF</span></li>
          <li><span><b>Chat with management</b>, who reply within seconds in the demo</span></li>
        </ul>
        <span class="btn gold">{I('phone')} Open the tenant demo</span>
        <span class="muted" style="font-size:13px">Best on a phone. On a computer it shows the desktop layout.</span>
      </a>
      <a class="dl reveal" href="demo/manager/" style="text-decoration:none;color:inherit">
        <div class="dl-head"><img class="app-icon" src="assets/img/app-manager.png" alt="TenantFlex Manager app icon"><div><h3>Management app</h3><span class="muted">You are Grace Wanjiru · Manager, Golden Gate Plaza</span></div></div>
        <div class="browser"><div class="bar"><i></i><i></i><i></i></div><img src="assets/img/manager-dashboard.jpg" alt="Management demo"></div>
        <ul class="checks">
          <li><span><b>See collections</b>, arrears and occupancy on the dashboard</span></li>
          <li><span><b>Confirm a bank transfer</b>, record cash, and bill rent or meter readings</span></li>
          <li><span><b>Message tenants</b> and post notices. A live M-Pesa payment arrives as you explore</span></li>
        </ul>
        <span class="btn gold">{I('dashboard')} Open the management demo</span>
      </a>
    </div>
    <p class="muted plan-note reveal">Like what you see? <a href="contact.html">Contact us</a> on WhatsApp +254 747 354 677 to get TenantFlex for your complex.</p>
  </div>
</section>
'''
open('demo.html','w').write(page('demo.html', 'Live demo · TenantFlex', 'Try the TenantFlex tenant app and management app live in your browser, with sample data.', demo_page))

def legal_page(fname, title, desc, body):
    html = f'''
<section class="page-head" style="padding-bottom:20px"><div class="wrap"><span class="eyebrow">Legal</span><h1>{title}</h1></div></section>
<section style="padding-top:0"><div class="wrap"><article class="legal">{body}</article></div></section>'''
    open(fname, 'w').write(page(fname, f'{title} · TenantFlex', desc, html))

legal_page('privacy.html', 'Privacy Policy', 'How Pizza Technologies handles personal data in TenantFlex, under the Kenya Data Protection Act, 2019.', legal.PRIVACY)
legal_page('terms.html', 'Terms of Use', 'Terms of Use for TenantFlex and TenantFlex Manager by Pizza Technologies.', legal.TERMS)
legal_page('data-processing.html', 'Data Processing Terms', 'Data Processing Terms between Pizza Technologies and complexes using TenantFlex (Kenya Data Protection Act, 2019, s.42).', legal.DPA)
legal_page('delete-account.html', 'Delete your account', 'How to delete your TenantFlex account and what happens to your data.', legal.DELETE)

open('404.html','w').write(page('404.html', 'Page not found · TenantFlex', 'Page not found.', f'''
<section class="page-head" style="min-height:60vh"><div class="wrap"><img src="assets/img/logo.png" alt="" style="width:120px"><h1>Page not found</h1><p class="lead">That page doesn't exist.</p><a class="btn gold" href="index.html">Back to home</a></div></section>'''))
print('pages written')
