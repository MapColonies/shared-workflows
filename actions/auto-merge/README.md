# Auto-merge PR by label

Checks if a pull request has the `auto-merge` label, waits for all checks to pass, and then merges the PR.

---

## ✨ What It Does

- Verifies the PR has the `auto-merge` label
- Waits for all PR checks to complete and pass
- Merges the PR with a squash strategy
- Skips merge if the label is missing or checks fail

---

## 🛠 Inputs

| Name | Description | Required | Default |
|------|-------------|----------|---------|
| `pr_number` | Pull Request number to check and merge | ✅ Yes |  |
| `github_token` | GitHub token with permissions to merge PRs | ✅ Yes |  |
| `repository` | Target repository in `owner/repo` format (typically `${{ github.repository }}`) | ✅ Yes |  |

---

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
permissions:
  contents: write
  pull-requests: write

steps:
  - name: Auto-merge PR by label
    uses: MapColonies/shared-workflows/actions/auto-merge@auto-merge-v0.1.0
    with:
      pr_number: ${{ github.event.pull_request.number }}
      github_token: ${{ secrets.GH_PAT }}
      repository: ${{ github.repository }}
```

<!-- x-release-please-end-version -->
