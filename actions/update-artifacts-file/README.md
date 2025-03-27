# 📦 Build and Push Helm Chart Action

This GitHub Action builds and publishes a Helm chart to a specified registry and updates an `artifacts.json` metadata file using custom shell scripts. 

---

## 🚀 What It Does

- Checks out the Helm chart repository
- Runs a script to update `artifacts.json` with the chart version and metadata
- Commits and pushes the updated metadata file to the repository

---

## 🔧 Inputs

| Name            | Description                                                    | Required | Default     |
|-----------------|----------------------------------------------------------------|----------|-------------|
| `scope`         | Logical scope or namespace used to group charts (comma-separated) | ✅ Yes   | `""`        |
| `repository`    | GitHub repository containing the Helm chart                   | ✅ Yes     | Current repo |
| `context`       | Path to the directory containing the Helm chart and scripts   | ✅ Yes   | `./helm`     |
| `type`          | Artifact type (`helm`, `docker`, etc.)                        | ✅ Yes     | `docker`     |
| `artifact-name` | The name of the chart to record in `artifacts.json`           | ✅ Yes   | —           |
| `artifact-tag`  | The chart version or tag                                      | ✅ Yes   | —           |
| `github_token`  | GitHub token used to commit and push changes                  | ✅ Yes   | —           |


---

## ✨ Usage

```yaml
- name: Update artifacts.json
uses: ./actions/update-artifacts-file
with:
    context: actions/update-artifacts-file
    scope: infra
    repository: ${{ env.action_repo }}
    artifact-name: "sftpgo"
    artifact-tag: "v2.0.2"
    registry: ${{ secrets.ACR_URL }}
    github_token: ${{ secrets.GH_PAT }}
```
