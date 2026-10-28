# TenantFlex iOS build

This branch builds the **TenantFlex** (tenant) and **TenantFlex Manager** iOS apps on a GitHub-hosted Mac.
It contains only the compiled web bundles (`apps/*/www`), the Capacitor configs and the app icons (gold on black for tenants, black on gold for the Manager) and splash screens. The app source lives in the private TenantFlex repository.

Each push runs `.github/workflows/ios.yml`. Download the results from the run's **Artifacts**:

| File | What it is |
|---|---|
| `*-unsigned.ipa` | Unsigned iPhone/iPad app. Before it will install on a device, sign it with an Apple Developer account (Xcode, AltStore, Sideloadly, or your MDM / App Store Connect pipeline). |
| `*-simulator.app.zip` | Runs in Xcode's iOS Simulator with no signing: unzip it and drag `App.app` onto a running Simulator. |

To update the apps, rebuild the web bundles in the TenantFlex repository (`npm run build`), then copy `web/dist/tenant` → `apps/tenant/www` and `web/dist/manager` → `apps/manager/www`.
