# Update site-values and create PR Action

This GitHub Action checks out a the MapColonies site-values repository (can be override), updates the chart version for a given service under a specific domain/environment file, and opens a pull request with the change.

---

## ✨ What It Does

- Checks out the target site-values repository (default: `MapColonies/site-values`)
- Updates the service chart version in `<domain>/environments/<environment>.yaml` to the provided tag
- Creates a pull request with the changes to the master branch with desired labels.

---

## 🛠 Inputs

| Name            | Description                                                                 | Required | Default                      |
|-----------------|-----------------------------------------------------------------------------|----------|------------------------------|
| `tag`           | Chart tag/version toc set for the service (e.g., `1.2.3`)                    | ✅ Yes   |                              |
| `domain`        | Domain folder inside the site-values repo (e.g., `raster`, `vector`, `app`) | ✅ Yes   |                              |
| `github_token`  | GitHub token with write access to the target repository                     | ✅ Yes   |                              |
| `repository`    | Target site-values repository (`owner/name`)                                | ❌ No    | `MapColonies/site-values`    |
| `branch`        | Base branch of the target repository                                        | ❌ No    | `master`                     |
| `service_repo`  | Service repository name to use as the key under `chartsVersions`            | ❌ No    | calling repo name            |
| `environment`   | Environment YAML to update under `environments/`                            | ❌ No    | `dev`                        |
| `pr_labels`     | Labels to apply on the created PR (newline or comma separated)              | ❌ No    | `dev`, `auto-merge`          |

> Note: If `service_repo` is not supplied, the action uses the calling repository name

---

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Update site-values and open PR
  uses: MapColonies/shared-workflows/actions/update-charts-pr@update-charts-pr-v1.0.0
  with:
    tag: 1.0.1
    domain: infra
    github_token: ${{ secrets.GH_PAT }}
    # Optional overrides
    # repository: MapColonies/site-values
    # branch: master
    # service_repo: test-repo
    # environment: dev
    # pr_labels: |
    #   dev
    #   auto-merge
```

<!-- x-release-please-end-version -->

---
