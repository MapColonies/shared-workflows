# Update site-values and create PR Action

This GitHub Action creates a PR for updating a chart version presented in a file.

---

## ✨ What It Does

- Checks out the target repository (default: `MapColonies/site-values`)
- Sets `chartsVersions[service_repo] = tag` in the YAML file at `update_path`
- Opens a pull request and applies optional labels

---

## 🛠 Inputs

| Name           | Description                                                                                  | Required | Default                   |
|----------------|----------------------------------------------------------------------------------------------|----------|---------------------------|
| `tag`          | Chart tag/version to set for the service (e.g., `1.2.3`)                                     | ✅ Yes   |                           |
| `paths`  | One or more YAML paths to update (e.g., `raster/environments/dev.yaml`)| ✅ Yes   |                           |
| `environment` | Deployment environment used for PR naming and messaging (`dev`, `prod`, etc.) | ✅ Yes |  |
| `github_token` | GitHub token with write access to the target repository                                      | ✅ Yes   |                           |
| `repository`   | Repository name (under `MapColonies/`) to update                                             | ❌ No    | `site-values`             |
| `branch`       | Base branch of the target repository                                                         | ❌ No    | `master`                  |
| `chart` | Chart name to use as the key under `chartsVersions`                             | ❌ No    | calling repo name         |
| `pr_labels`    | Labels to apply on the created PR (comma separated)                                          | ❌ No    |        |
| `reviewers`    | Comma-separated GitHub usernames to request review from (used only if non-empty)            | ❌ No    |        |
| `assignees`    | Comma-separated GitHub usernames to assign to the PR (used only if non-empty)              | ❌ No    |        |

> Branch naming: When `environment` is `prod`, the pull request branch will be named `prod`. Otherwise, the branch will be `<environment>-<chart>-<sha>` (e.g., `dev-my-service-<commit-sha>`).

---

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Update site-values and open PR
  uses: MapColonies/shared-workflows/actions/update-chart-version@update-chart-version-v1.0.0
  with:
    tag: 1.0.0
    paths: |
        infra/environments/dev.yaml
        common/environments/dev.yaml
    github_token: ${{ secrets.GH_PAT }}
    environment: dev
```

<!-- x-release-please-end-version -->
