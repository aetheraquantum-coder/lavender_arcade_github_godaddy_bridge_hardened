# Lavender Arcade Games — GoDaddy Upload Package

This ZIP is structured so `index.html` is at the ZIP root.

## Upload through GoDaddy cPanel

1. Open GoDaddy > My Products > Web Hosting > Manage.
2. Open cPanel / File Manager.
3. Open the document root for the domain (often `public_html`).
4. Upload the ZIP.
5. Extract the ZIP directly into the document root.
6. Confirm that `index.html` is directly inside the document root.
7. Visit your domain.

## Included

- Main responsive arcade catalog
- Age filters: Under 13, 13–16, 17+, 18+
- Controller/browser/homebrew/learning filters
- Kid-friendly game concepts
- Fantasy, zombie/alliance, Interstellar, spy-college, and translation concepts
- Emulator/homebrew policy language
- Creator submission guide
- Privacy page
- Configurable jurisdiction-rules JSON
- No external JavaScript libraries, fonts, trackers, or CDNs

## Important production notes

This is a static storefront package. Real accounts, payments, creator uploads, multiplayer, cloud saves, age verification, and jurisdiction enforcement require a backend.

Do not treat `data/jurisdiction-rules.json` as legal advice. Populate it only after validating the rules that apply to your business.

For Tor/onion hosting, mirror the same static package on a VPS running Tor. Shared cPanel hosting generally should not be treated as the onion-service host.

For emulator compatibility, distribute only software you are legally authorized to distribute, such as original homebrew, public-domain software, and authorized ports.
