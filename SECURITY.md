# Security Policy

## Supported versions
| Installer | Status |
|-----------|--------|
| 2.4.x     | supported |
| <= 2.3    | EOL |

## Reporting a vulnerability
Email security@jennymod.dev with:
- Affected version
- Reproduction steps
- Impact assessment

We aim to acknowledge within 72h and patch within 14 days for confirmed issues.

## Integrity
Every artifact in `jenny_manifest.json` is pinned by SHA-256. The installer
refuses to place any jar that fails checksum verification. Do **not** disable
verification — patched jars are a common malware vector for mod installers.