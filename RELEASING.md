# Releasing

## Stable release checklist

1. Make sure `main` is green in GitHub Actions.
2. Confirm `custom_components/pymc_repeater/manifest.json` has the intended version.
3. Update `CHANGELOG.md` if needed.
4. Create a Git tag matching the release version, for example `v1.0.0`.
5. Create a GitHub release from that tag.
6. Copy the matching changelog section into the release notes if you want custom notes.

## Notes

- HACS works better with full GitHub releases than with branch-only installs.
- Dependabot will keep the GitHub Actions workflow dependencies up to date automatically.
