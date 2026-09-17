# Lavender Arcade GitHub → GoDaddy Bridge

This repository package connects a GitHub repository to GoDaddy in two ways:

1. **Automatic website deployment** to GoDaddy Web Hosting (cPanel) over FTPS.
2. **Read-only DNS diagnostics** through GoDaddy Domains API v3.

The actual Lavender Arcade site lives in `site/`.

## 1. Create a GitHub repository

Create a new repository, then upload the contents of this package so these paths exist:

- `.github/workflows/deploy-godaddy.yml`
- `.github/workflows/godaddy-dns-read.yml`
- `scripts/godaddy_dns_read.py`
- `site/index.html`

Push to the `main` branch.

## 2. Add GoDaddy FTP credentials as GitHub Actions secrets

In GitHub:

`Repository → Settings → Secrets and variables → Actions → Secrets`

Create:

- `GODADDY_FTP_HOST`
- `GODADDY_FTP_USER`
- `GODADDY_FTP_PASSWORD`

Use the FTP/cPanel values from your GoDaddy Web Hosting dashboard.

Do **not** commit FTP credentials into this repository.

## 3. Set the GoDaddy remote directory

In:

`Repository → Settings → Secrets and variables → Actions → Variables`

Create:

- `GODADDY_REMOTE_DIR` = `public_html`

If your GoDaddy FTP account starts inside the document root already, set this to `.` instead.

## 4. Automatic deployment

Any push to `main` that changes `site/**` starts the deployment workflow.

You can also run it manually from:

`GitHub → Actions → Deploy Lavender Arcade to GoDaddy → Run workflow`

The workflow mirrors `site/` into the configured GoDaddy directory.

### Important

The deploy command uses `--delete`, so a file deleted from `site/` will also be removed from the GoDaddy target directory. This keeps GitHub as the source of truth.

For a first test, use a separate GoDaddy subdomain or staging directory if available.

## 5. Optional GoDaddy DNS API diagnostics

GoDaddy Domains API v3 supports PAT authentication.

Create a GoDaddy Personal Access Token with the minimum read scope needed for DNS/domain reads.

Add the token as a GitHub secret:

- `GODADDY_PAT`

Add this GitHub Actions variable:

- `GODADDY_DOMAIN` = `lavenderarcadegames.com`

Then manually run:

`GitHub → Actions → GoDaddy DNS Diagnostic → Run workflow`

This workflow only performs a GET request and does not edit DNS.

## Security model

- FTP credentials are GitHub Actions secrets.
- The GoDaddy PAT is a separate GitHub Actions secret.
- The included DNS helper is read-only.
- GitHub workflow permissions are `contents: read`.
- No credentials are stored in the website files.
- Use GitHub environment protection for `production` if your plan supports it.
- Give GoDaddy API tokens only the scopes actually required.

## Editing the arcade

Edit anything inside `site/`, commit, and push to `main`.

Typical flow:

1. Edit `site/index.html` or a game under `site/games/`.
2. Commit changes.
3. Push to `main`.
4. GitHub Actions uploads the new version to GoDaddy.

## Emulator/homebrew builds

Put lawful downloadable homebrew artifacts in a dedicated site folder, for example:

`site/downloads/homebrew/`

Only distribute content you have permission to distribute.

## Tor

This workflow deploys the public GoDaddy website. A Tor onion service should remain on a separate VPS where you can run the Tor daemon. You can mirror the same `site/` directory there with a second deployment workflow later.

## HTTP-compatible security profile

The public static catalog is intentionally able to render over plain HTTP for
legacy or constrained environments. It does not rely on secure-context-only
browser features.

The included `.htaccess` sets:
- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- X-Frame-Options
- Cross-Origin-Opener-Policy
- Cross-Origin-Resource-Policy

HSTS is only enabled when HTTPS is active.

Important: HTTP cannot provide transport confidentiality or server
authentication. Keep logins, payments, authenticated uploads, age-verification
data, and any sensitive account/API operations HTTPS-only.

## Current GitHub connector status

The ChatGPT GitHub connection is authenticated, but no repositories are
currently exposed to the connector. Grant the GitHub app access to the target
repository before expecting direct repository updates from ChatGPT.
