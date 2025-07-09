# Update Artifacts File Action

This GitHub Action builds and publishes a Helm chart to a specified registry and updates an `artifacts.json` metadata file using custom shell scripts. 

---

## ✨ What It Does

- Checks out the Helm chart repository
- Runs a script to update `artifacts.json` with the chart version and metadata
- Commits and pushes the updated metadata file to the repository

---

## 🛠 Inputs

| Name             | Description                                                                 | Required | Default                      |
|------------------|-----------------------------------------------------------------------------|----------|------------------------------|
| `domain`         | Logical scope or namespace for the artifact (used as subdirectory name)     | ✅ Yes   |                              |
| `artifact_name`  | Name of the artifact (e.g. `sftpgo`, `minio`)                               | ✅ Yes   |                              |
| `artifact_tag`   | Tag or version of the artifact (e.g. `v1.2.3`, `latest`)                    | ✅ Yes   |                              |
| `type`           | Type of artifact (`helm`, `docker`, etc.)                                   | ✅ Yes   |                              |
| `registry`       | Registry URL the artifact is pushed to (e.g., ACR address)                  | ✅ Yes   |                              |
| `github_token`   | GitHub token with permission to clone, commit & push to the target repo     | ✅ Yes   |                              |
| `target_repo`    | Target GitHub repo where `artifacts.json` should be updated (e.g. `org/repo`)| ❌ No    | `mapcolonies/helm-charts`   |
| `target_branch`  | Target branch in the repository to update                                   | ❌ No    | `master`                     |

---

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Update artifacts.json
  uses: MapColonies/shared-workflows/actions/update-artifacts-file@update-artifacts-file-v1.1.1
  with:
    domain: infra
    artifact_name: "sftpgo"
    artifact_tag: "version"
    type: "docker"
    registry: ${{ secrets.ACR_URL }}
    github_token: ${{ secrets.GH_PAT }}
```
<!-- x-release-please-end-version -->
