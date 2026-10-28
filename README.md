# TenantFlex website

The public website for **TenantFlex**: tenancy, billing and payments for business and shopping complexes.

- `index.html`: product showcase (tenant app, manager app, payments, billing automation, communication, platforms, FAQ)
- `features.html`: every screen of both apps
- `contact.html`: contact details (WhatsApp +254 747 354 677, info@pizzatechnologies.co.ke) and the onboarding steps

It's a static site with no build step. Preview it locally with `python3 -m http.server` and open http://localhost:8000.

## Publishing with GitHub Pages
Settings → Pages → *Build and deployment* → Source: **Deploy from a branch** → Branch: **gh-pages** / **(root)** → Save.
The site is then served at `https://pizzatechies.github.io/flexhub/`.

Screenshots in `assets/img/` were taken from the real TenantFlex apps using the Golden Gate Plaza demo complex.
