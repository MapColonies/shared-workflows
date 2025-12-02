# Update site-values and create PR Action

This GitHub Action checks out the MapColonies site-values repository (can be overridden),
updates the chart version for a given service under a specific domain/environment file, 
and opens a pull request with the change.

---

## ✨ What It Does

- Checks out the target site-values repository (default: `MapColonies/site-values`)
- Updates the service chart version in the file specified by `update_path` (e.g., `<domain>/environments/<environment>.yaml`) to the provided tag
- Creates a pull request with the changes to the master branch with desired labels.

---

## 🛠 Inputs

| Name           | Description                                                                                  | Required | Default                   |
|----------------|----------------------------------------------------------------------------------------------|----------|---------------------------|
| `tag`          | Chart tag/version to set for the service (e.g., `1.2.3`)                                     | ✅ Yes   |                           |
| `update_path`  | Path (relative to repo root) to the YAML file to update (e.g., `raster/environments/dev.yaml`)| ✅ Yes   |                           |
| `github_token` | GitHub token with write access to the target repository                                      | ✅ Yes   |                           |
| `repository`   | Repository name (under `MapColonies/`) to update                                             | ❌ No    | `site-values`             |
| `branch`       | Base branch of the target repository                                                         | ❌ No    | `master`                  |
| `service_repo` | Service repository name to use as the key under `chartsVersions`                             | ❌ No    | calling repo name         |
| `pr_labels`    | Labels to apply on the created PR (comma separated)                                          | ❌ No    | `dev`, `auto-merge`       |

> Note: If `service_repo` is not supplied, the action uses the calling repository name.

---

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Update site-values and open PR
  uses: MapColonies/shared-workflows/actions/update-charts-pr@update-charts-pr-v1.0.0
  with:
    tag: 1.0.1
    update_path: infra/environments/dev.yaml
    github_token: ${{ secrets.GH_PAT }}
    # # Optional overrides
    # repository: site-values
    # branch: master
    # service_repo: test-repo
    # pr_labels: dev, auto-merge
```

<!-- x-release-please-end-version -->
