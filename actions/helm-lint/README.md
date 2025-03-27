# Lint and Test Helm Charts Action

This GitHub Action uses [chart-testing (ct)](https://github.com/helm/chart-testing) and [kind](https://kind.sigs.k8s.io/) 
to lint and install Helm charts in a Kubernetes-in-Docker cluster.

It detects which charts have changed and only tests those.

## 🛠 Inputs

| Name         | Description                                                  | Required | Default |
|--------------|--------------------------------------------------------------|----------|---------|
| `chartDirs`  | Comma-separated list of root directories with Helm charts.   | ✅ Yes     | `.`     |
| `repository` | The full GitHub repository (e.g. `MapColonies/helm-charts`) containing the Helm chart | ✅ Yes   |     |

## 📤 Outputs

| Name     | Description                          |
|----------|--------------------------------------|
| `changed`| Whether any charts were changed.     |

## 🚀 Usage

```yaml
- name: Lint and Test Charts
  uses: MapColonies/shared-workflows/actions/helm-lint@helm-lint-v1
  with:
    chartDirs: infra/monitoring,infra/sftpgo
    repository: ${{ github.repository }}
```
