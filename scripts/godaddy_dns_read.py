#!/usr/bin/env python3
"""
Read-only GoDaddy Domains API v3 DNS diagnostic.

Requires:
  GODADDY_PAT environment variable
Usage:
  python3 scripts/godaddy_dns_read.py example.com
"""

import json
import os
import sys
import urllib.parse
import urllib.request
import urllib.error

API = "https://api.godaddy.com/v3/domains/zones/{zone}/dns-records?pageSize=100"

def main():
    if len(sys.argv) != 2:
        print("Usage: godaddy_dns_read.py DOMAIN", file=sys.stderr)
        return 2

    domain = sys.argv[1].strip().lower()
    token = os.environ.get("GODADDY_PAT", "").strip()

    if not domain or "." not in domain:
        print("Invalid domain.", file=sys.stderr)
        return 2
    if not token:
        print("Missing GODADDY_PAT.", file=sys.stderr)
        return 2

    url = API.format(zone=urllib.parse.quote(domain, safe=".-"))
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/json",
            "User-Agent": "lavender-arcade-github-godaddy-bridge/1.0",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print("GoDaddy API error:", exc.code, file=sys.stderr)
        print(body[:2000], file=sys.stderr)
        return 1
    except Exception as exc:
        print("Request failed:", str(exc), file=sys.stderr)
        return 1

    items = payload.get("items", [])
    safe_rows = []
    for item in items:
        safe_rows.append({
            "recordId": item.get("recordId"),
            "type": item.get("type"),
            "name": item.get("name"),
            "data": item.get("data"),
            "ttl": item.get("ttl"),
        })

    print(json.dumps({
        "domain": domain,
        "record_count": len(safe_rows),
        "records": safe_rows,
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
