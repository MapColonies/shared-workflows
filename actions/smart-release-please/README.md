# Smart Release Please

This GitHub Action is a wrapper around [googleapis/release-please-action](https://github.com/googleapis/release-please-action).
It's designed to enforce a specific versioning strategy for release candidates (RCs) on the `next` branch.

It computes the intended `Release-As:` version from commit history and injects a bot commit if necessary to align RC versions before delegating to Release Please.

## ✨ How It Works
- Find the baseline tag:
  - Use the latest RC tag like `vX.Y.Z-rc.N`; otherwise the latest stable tag `vX.Y.Z`. If there are no tags, treat the baseline as `0.0.0`.
- Count real commits since the baseline (ignores bot commits and commits with a `Release-As:` footer).
- Read commit messages based on SemVer
- Decide the next version (RC tags look like `vMAJOR.MINOR.PATCH-rc.N`):
- Apply the version on `next`

## 🛠 Inputs

| Name    | Description                                                       | Required | Default            |
|---------|-------------------------------------------------------------------|----------|--------------------|
| `token` | GitHub Token (PAT) for pushing commits and triggering releases. It can be passed in order to trigger workflows after this one  | No       | `${{ github.token }}` |

## 🚀 Usage
Add a workflow that runs on your RC branch (e.g., `next`) and uses this action:

```yaml
name: Smart Release Please

on:
  push:
    branches:
      - next

permissions:
  contents: write

jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v6
        with:
          fetch-depth: 0

      - name: Run Smart Release Please
        uses: MapColonies/shared-workflows/actions/smart-release-please@smart-release-please-v1.0.0
        with:
          token: ${{ secrets.GH_PAT }}
```
> Note: Ensure your repository contains `release-please-config.next.json` (and the appropriate `release-please-config.<branch>.json`).
