# Legal pages for the TenantFlex website. Plain HTML fragments; page chrome comes from mksite.py.
EFFECTIVE = '29 October 2026'
EMAIL = 'info@pizzatechnologies.co.ke'
WA = '+254 747 354 677'
CONTACT = f'<a href="mailto:{EMAIL}">{EMAIL}</a> or WhatsApp <a href="https://wa.me/254747354677" target="_blank" rel="noopener">{WA}</a>'

PRIVACY = f'''
<p class="legal-meta">Effective {EFFECTIVE}</p>
<p>This Privacy Policy explains how <b>Pizza Technologies</b> ("we", "us"), a company registered in Kenya, handles personal data in <b>TenantFlex</b>: the TenantFlex tenant app, the TenantFlex Manager app, their web versions, the TenantFlex servers we operate, and this website. It is written to meet the Kenya Data Protection Act, 2019 (the "Act") and its regulations.</p>

<h2>1. Who is responsible for your data</h2>
<ul>
<li><b>Tenant data inside a complex.</b> Each business or shopping complex ("the complex") that uses TenantFlex decides what tenant data to collect and why, such as bills, payments, units and messages. For that data <b>the complex is the data controller</b> and Pizza Technologies is its <b>data processor</b>: we process it only on the complex's instructions, under our <a href="data-processing.html">Data Processing Terms</a>. For questions about your tenancy records, contact your complex's management first. You can also contact us and we will help.</li>
<li><b>Everything else.</b> For management accounts, subscriptions and billing of complexes, support enquiries, and this website, <b>Pizza Technologies is the data controller</b>.</li>
</ul>

<h2>2. What we collect</h2>
<table class="legal-table">
<tr><th>Category</th><th>Examples</th><th>Source</th></tr>
<tr><td>Account details</td><td>Name, business name, email address, phone number, role (tenant or manager), password (stored only as a secure hash)</td><td>You, or your complex's management when they create your account</td></tr>
<tr><td>Tenancy and billing records</td><td>Your complex, unit(s), rent, electricity and water bills, meter readings, other charges, due dates and balances</td><td>Your complex's management</td></tr>
<tr><td>Payment records</td><td>Amounts, payment method, M-Pesa phone number, M-Pesa receipt number, bank transfer reference, receipt numbers. We never store full card numbers</td><td>You, the complex, and Safaricom (M-Pesa confirmations)</td></tr>
<tr><td>Messages and notices</td><td>Messages between tenants and management, notices from the complex, in-app notifications</td><td>You and your complex</td></tr>
<tr><td>Consent and security records</td><td>When you accepted these terms, sign-in activity, IP address (used briefly to block password-guessing), server logs</td><td>Your device and our servers</td></tr>
<tr><td>Integration credentials (complexes only)</td><td>M-Pesa Daraja shortcode, consumer key, consumer secret and passkey, stored encrypted</td><td>Complex management</td></tr>
<tr><td>Enquiries</td><td>Your name, contact details and message when you WhatsApp or email us</td><td>You</td></tr>
</table>
<p>We do not collect your location, contacts, photos or advertising identifiers, and TenantFlex contains no advertising or third-party tracking.</p>

<h2>3. How we use it, and our lawful basis</h2>
<ul>
<li><b>To provide TenantFlex</b>: showing bills, taking payments, issuing receipts, delivering messages and notifications, and running management dashboards. Basis: performance of a contract (s.30(1)(b)(i) of the Act), on behalf of your complex.</li>
<li><b>To process payments</b>: sending the amount and your M-Pesa number to Safaricom so you get the PIN prompt, then recording Safaricom's confirmation. Basis: contract.</li>
<li><b>To keep records required by law</b>: financial and tax records. Basis: legal obligation.</li>
<li><b>To keep TenantFlex secure</b>: preventing fraud and unauthorised access, and fixing faults. Basis: legitimate interests.</li>
<li><b>To support and bill complexes</b>: answering enquiries and invoicing subscriptions. Basis: contract and legitimate interests.</li>
</ul>
<p>We do not sell personal data, use it for advertising, or use it to make automated decisions with legal effects on you.</p>

<h2>4. Who we share it with</h2>
<ul>
<li><b>Your complex's management</b> sees the data of its own tenants. Other complexes never see it.</li>
<li><b>Safaricom PLC</b> receives the phone number and amount needed to process M-Pesa payments, and handles them under its own privacy statement.</li>
<li><b>Hosting providers</b> that run our servers and database (for example Render Services, Inc.) act as our sub-processors under contracts that require them to protect the data.</li>
<li><b>Banks</b>: when you pay by bank transfer, your reference is shared with the complex so it can match the payment.</li>
<li><b>Authorities</b>, when the law requires it, such as a court order or a tax or regulatory request.</li>
</ul>

<h2>5. Transfers outside Kenya</h2>
<p>Our servers may be hosted outside Kenya, for example in the United States or the European Union. Where data is transferred outside Kenya, we do so in line with sections 48–50 of the Act. We use providers that give appropriate safeguards for the security and protection of personal data, and we transfer only what is needed to run TenantFlex.</p>

<h2>6. How long we keep it</h2>
<ul>
<li><b>Account details</b>: while the account is active. When you delete your account they are erased (see <a href="delete-account.html">Delete your account</a>).</li>
<li><b>Bills, payments and receipts</b>: kept for at least <b>five years</b> after the transaction, as Kenyan tax law requires business records to be kept. After an account is deleted, these records are kept without the person's name and contact details.</li>
<li><b>Messages and notifications</b>: until the account is deleted or the complex closes its TenantFlex account.</li>
<li><b>Technical logs</b>: kept briefly, only for security and troubleshooting.</li>
<li>When a complex leaves TenantFlex, its data is returned or deleted as set out in the Data Processing Terms, except records we must keep by law.</li>
</ul>

<h2>7. How we protect it</h2>
<p>All connections are encrypted (HTTPS). Passwords are stored as one-way scrypt hashes, and M-Pesa credentials are encrypted with AES-256-GCM. Each complex's data is kept separate from every other complex, and tenants can see only their own records. Sign-in attempts are rate-limited, and access to production systems is restricted to authorised Pizza Technologies staff. No system is perfectly secure. If a personal data breach occurs, we will notify the affected complex, the Office of the Data Protection Commissioner and, where required, you, as set out in section 43 of the Act.</p>

<h2>8. Your rights</h2>
<p>Under the Act you have the right to:</p>
<ul>
<li>be informed about how your data is used (this policy)</li>
<li><b>access</b> your data. Use <b>Account → Privacy &amp; data → Download my data</b> in the app, or ask us</li>
<li><b>correct</b> inaccurate data. Edit your profile in the app, or ask your complex to correct bills</li>
<li><b>delete</b> your data. Use <b>Account → Delete my account</b>, or see <a href="delete-account.html">Delete your account</a></li>
<li>object to processing, or withdraw consent where processing relies on consent</li>
<li><b>data portability</b>: your export is a machine-readable JSON file</li>
</ul>
<p>To exercise a right, contact {CONTACT}. We may need to verify your identity, and we respond within the timelines set by the Data Protection (General) Regulations, 2021. You can also complain to the <b>Office of the Data Protection Commissioner</b> (<a href="https://www.odpc.go.ke" target="_blank" rel="noopener">www.odpc.go.ke</a>).</p>

<h2>9. On your device and on this website</h2>
<p>The apps store only what they need to work on your device: your sign-in token and the address of your TenantFlex server. This website uses no cookies, analytics or advertising. It is hosted on GitHub Pages and loads fonts from Google Fonts, which receive your IP address to deliver those files. The live demos on this website run entirely in your browser with sample data: nothing you do in a demo is sent to us.</p>

<h2>10. Children</h2>
<p>TenantFlex is for businesses and adults. It is not directed at children under 18, and we do not knowingly collect their data.</p>

<h2>11. Changes</h2>
<p>We will post any changes here with a new effective date. If changes are significant, we will tell you in the app and ask you to accept them again.</p>

<h2>12. Contact</h2>
<p>Pizza Technologies, Kenya · {CONTACT}</p>
'''

TERMS = f'''
<p class="legal-meta">Effective {EFFECTIVE}</p>
<p>These Terms of Use ("Terms") govern your use of <b>TenantFlex</b>, provided by <b>Pizza Technologies</b>, a company registered in Kenya ("we", "us"). That covers the TenantFlex and TenantFlex Manager apps (Android, iOS, Windows and web), our servers and this website. By creating an account or using TenantFlex you agree to these Terms and to our <a href="privacy.html">Privacy Policy</a>.</p>

<h2>1. Who's who</h2>
<ul>
<li><b>Complex</b>: a business or shopping complex, landlord or property manager that subscribes to TenantFlex. Its staff use TenantFlex Manager.</li>
<li><b>Tenant</b>: a business or person renting space in a complex who uses the TenantFlex app at the complex's invitation.</li>
<li>Pizza Technologies provides the software. <b>We are not a party to any tenancy, lease or service agreement</b> between a complex and its tenants.</li>
</ul>

<h2>2. Accounts</h2>
<ul>
<li>You must give accurate details and keep your password secret. You are responsible for activity on your account.</li>
<li>Complex management may create, reset or deactivate tenant accounts for their complex. A temporary password from management must be changed when you first sign in.</li>
<li>Tell us or your complex straight away if you think your account has been misused.</li>
<li>You can delete your account at any time in the app (see <a href="delete-account.html">Delete your account</a>).</li>
</ul>

<h2>3. Bills, payments and receipts</h2>
<ul>
<li><b>Bills are issued by the complex</b>, not by Pizza Technologies. Questions or disputes about rent, utilities or other charges must be raised with your complex's management.</li>
<li><b>Payments go directly to the complex</b>, to its M-Pesa Paybill or Till, or its bank account. <b>Pizza Technologies does not receive, hold or transfer tenants' money.</b> Refunds are handled by the complex.</li>
<li><b>M-Pesa</b> payments are processed by Safaricom under its own terms. M-Pesa charges whole shillings, so amounts with cents are rounded up to the next shilling and the receipt shows both amounts. Safaricom's transaction charges, if any, are set by Safaricom.</li>
<li><b>Bank transfers</b> are confirmed by the complex once the money reaches its account. The receipt is issued at that point.</li>
<li>A TenantFlex <b>receipt</b> confirms that the payment was received and recorded against your bills. Tax invoices, where required, are issued by the complex through its own tax systems.</li>
<li>If a payment fails, is reversed or is found to be fraudulent, the complex may cancel the related receipt and reinstate the balance.</li>
</ul>

<h2>4. Subscriptions (complexes)</h2>
<ul>
<li>Complexes pay a subscription for TenantFlex on a monthly or annual plan as shown on our <a href="pricing.html">pricing page</a> or in a written quote. Fees are in Kenyan Shillings and payable in advance. Applicable taxes are added as required by law.</li>
<li>Plans renew automatically at the end of each billing period unless cancelled before renewal. Cancellation takes effect at the end of the paid period, and fees already paid for a period are not refundable unless the law requires otherwise.</li>
<li>We may change prices with at least 30 days' notice. The new price applies from your next billing period.</li>
<li>If fees remain unpaid 14 days after the due date, we may suspend the complex's access after giving notice. Tenants' records are kept safe during any suspension.</li>
<li>Each complex is responsible for its own TenantFlex usage, its M-Pesa and bank arrangements, and its obligations to its tenants, including notices required under data protection law.</li>
</ul>

<h2>5. Acceptable use</h2>
<p>You must not misuse TenantFlex. In particular, you must not: break the law or anyone's rights; upload false, abusive or malicious content; try to access other people's accounts or data; interfere with or overload our systems; probe or test their security without our written permission; reverse-engineer the software except where the law allows; or use TenantFlex to send spam. We may suspend accounts that do.</p>

<h2>6. Your data</h2>
<p>Each complex owns the data it puts into TenantFlex, and each person owns their own details. You give us permission to store and process that data only to provide TenantFlex, as described in our <a href="privacy.html">Privacy Policy</a> and, for complexes, our <a href="data-processing.html">Data Processing Terms</a>. Complexes and tenants can export their data from the apps.</p>

<h2>7. Availability and changes</h2>
<p>We work to keep TenantFlex available and secure, but it may sometimes be unavailable, for example during maintenance, network or M-Pesa outages, or events beyond our control. We may improve or change features. If we remove a major feature a complex pays for, we will give reasonable notice.</p>

<h2>8. Intellectual property</h2>
<p>TenantFlex, its software, design, logos and content belong to Pizza Technologies or its licensors. We give you a personal, non-exclusive, non-transferable right to use TenantFlex in line with these Terms.</p>

<h2>9. Suspension and ending</h2>
<p>You can stop using TenantFlex at any time. We may suspend or end access for a serious or repeated breach of these Terms, for non-payment of subscription fees, or where the law requires it. Where reasonable, we will warn you first. When a complex leaves, it can export its data for 30 days. After that, the data is deleted except records we must keep by law.</p>

<h2>10. Disclaimers and liability</h2>
<ul>
<li>TenantFlex is provided with reasonable skill and care, but we do not promise that it will be uninterrupted or error-free. We are not responsible for the services of third parties such as Safaricom, banks, app stores or internet providers.</li>
<li>To the extent the law allows, we are not liable for indirect or consequential losses, or for loss of profit or business. Our total liability to a complex in any 12-month period is limited to the subscription fees it paid us in that period. These limits do not apply to liability that cannot be limited by law, and nothing in these Terms affects your rights under the Consumer Protection Act, 2012.</li>
<li>Complexes are responsible for the accuracy of the bills they issue and for their dealings with tenants.</li>
</ul>

<h2>11. Law and disputes</h2>
<p>These Terms are governed by the laws of Kenya. If a dispute arises, please contact us first and we will try to resolve it amicably within 30 days. If it can't be resolved, it will be decided by the courts of Kenya.</p>

<h2>12. Changes to these Terms</h2>
<p>We may update these Terms. We will post changes here with a new effective date and, for significant changes, tell you in the app. Continuing to use TenantFlex after the effective date means you accept the updated Terms.</p>

<h2>13. Contact</h2>
<p>Pizza Technologies, Kenya · {CONTACT}</p>
'''

DPA = f'''
<p class="legal-meta">Effective {EFFECTIVE}</p>
<p>These Data Processing Terms form part of the agreement between <b>Pizza Technologies</b> ("Processor") and each complex that uses TenantFlex ("Controller"). They apply when Pizza Technologies processes personal data on the complex's behalf, as required by section 42 of the Kenya Data Protection Act, 2019 (the "Act"). The person who registers a complex, or accepts these terms in TenantFlex Manager, confirms they are authorised to accept them for the complex.</p>

<h2>1. Scope of processing</h2>
<table class="legal-table">
<tr><td><b>Subject matter</b></td><td>Hosting and operating TenantFlex for the Controller's complex.</td></tr>
<tr><td><b>Duration</b></td><td>While the Controller uses TenantFlex, plus the return and deletion period in clause 8.</td></tr>
<tr><td><b>Nature and purpose</b></td><td>Storing, organising, displaying and transmitting data to manage tenancies, issue bills, collect payments, issue receipts, and communicate with tenants.</td></tr>
<tr><td><b>Data subjects</b></td><td>The Controller's tenants and their contact persons, and the Controller's staff who use TenantFlex Manager.</td></tr>
<tr><td><b>Personal data</b></td><td>Names, business names, email addresses, phone numbers, unit and tenancy details, bills and meter readings, payment records (including M-Pesa numbers and receipt numbers), messages and notifications.</td></tr>
<tr><td><b>Sensitive data</b></td><td>None is required. The Controller should not enter sensitive personal data into TenantFlex.</td></tr>
</table>

<h2>2. Instructions</h2>
<p>The Processor processes personal data only on the Controller's documented instructions. Those instructions are given by configuring and using TenantFlex and through these terms. The Processor also processes it where Kenyan law requires, in which case it will tell the Controller unless the law forbids it. The Processor will tell the Controller if it believes an instruction breaks the Act.</p>

<h2>3. Confidentiality</h2>
<p>Only authorised Pizza Technologies personnel who need it to provide or support TenantFlex can access the personal data, and they are bound by confidentiality.</p>

<h2>4. Security</h2>
<p>The Processor maintains appropriate technical and organisational measures (section 41 of the Act). These include:</p>
<ul>
<li>encryption in transit (HTTPS)</li>
<li>password hashing, and encryption of integration credentials at rest</li>
<li>logical separation of each complex's data, and role-based access</li>
<li>sign-in rate limiting and restricted production access</li>
<li>backups provided by its hosting provider</li>
<li>regular review of these measures</li>
</ul>

<h2>5. Sub-processors</h2>
<p>The Controller authorises the Processor to use sub-processors that host TenantFlex's servers and database (currently Render Services, Inc.). The Processor will bind each sub-processor to data protection obligations at least as protective as these, will remain responsible for them, and will give notice of new sub-processors so the Controller can object on reasonable grounds. Safaricom PLC processes M-Pesa payments as an independent controller under its own terms; it is not a sub-processor.</p>

<h2>6. Transfers outside Kenya</h2>
<p>Data may be hosted outside Kenya. The Processor ensures any such transfer complies with sections 48–50 of the Act and uses providers offering appropriate safeguards.</p>

<h2>7. Assistance</h2>
<ul>
<li><b>Data subject requests</b>: TenantFlex lets tenants export and delete their own data. The Processor will help the Controller answer other requests under sections 26 to 40 of the Act, and will pass on any request it receives directly.</li>
<li><b>Breaches</b>: the Processor will notify the Controller without undue delay, and in any case within 48 hours, of becoming aware of a personal data breach. It will provide the information needed for the Controller's notification to the Data Commissioner under section 43 of the Act.</li>
<li>The Processor will reasonably help with data protection impact assessments and with enquiries from the Data Commissioner.</li>
</ul>

<h2>8. Return and deletion</h2>
<p>When the Controller stops using TenantFlex, it can export its data for 30 days. After that, the Processor deletes the Controller's personal data, except where Kenyan law requires it to be retained. Such records are kept only as long as required, and protected.</p>

<h2>9. Information and audits</h2>
<p>The Processor will make available the information reasonably needed to show compliance with these terms, and will answer the Controller's reasonable written questions. On-site audits require reasonable notice and must respect the confidentiality and security of other customers.</p>

<h2>10. Controller's responsibilities</h2>
<p>The Controller confirms it has a lawful basis for the personal data it puts into TenantFlex. It will inform its tenants how their data is used (it may refer them to the TenantFlex <a href="privacy.html">Privacy Policy</a>) and keep its data accurate. Where the Act requires, it will be registered with the Office of the Data Protection Commissioner.</p>

<h2>11. Contact</h2>
<p>Data protection questions: {CONTACT}</p>
'''

DELETE = f'''
<p class="legal-meta">For TenantFlex and TenantFlex Manager · Pizza Technologies</p>
<p>You can delete your TenantFlex account yourself at any time, directly in the app.</p>

<h2>Delete your account in the app</h2>
<ol>
<li>Open <b>TenantFlex</b> or <b>TenantFlex Manager</b> and sign in.</li>
<li>Go to <b>Account</b>. On a phone it's under <b>More → Account</b>; in TenantFlex Manager it's at the bottom of <b>Settings</b>.</li>
<li>Under <b>Privacy &amp; data</b>, tap <b>Delete my account</b>.</li>
<li>Enter your password and tap <b>Delete account</b>. You'll be signed out straight away.</li>
</ol>
<p>Before deleting, you can tap <b>Download my data</b> to keep a copy.</p>

<h2>Can't get into the app?</h2>
<p>Contact us on {CONTACT} from the phone number or email address on your account, and tell us your complex's name. We'll confirm it's you and delete the account within the timelines required by the Kenya Data Protection Act. If you've only forgotten your password, your complex's management can reset it for you.</p>

<h2>What is deleted, and what is kept</h2>
<ul>
<li><b>Deleted:</b> your name, business name, email address, phone number, password, messages and notifications. Your unit is released.</li>
<li><b>Kept, without your name or contact details:</b> bills, payments and receipts. Kenyan tax law requires the complex to keep payment records for at least five years, and they are deleted after that.</li>
<li>Deleting your account does <b>not</b> cancel money owed to your complex. Please settle balances with your complex's management.</li>
<li>Complex managers: the last manager of a complex can't delete their own account. Add another manager first, or contact us to close the complex's TenantFlex account.</li>
</ul>
<p>More detail is in our <a href="privacy.html">Privacy Policy</a>.</p>
'''
