# Lint and Test Helm Charts Action

This GitHub Action uses [chart-testing (ct)](https://github.com/helm/chart-testing) and [kind](https://kind.sigs.k8s.io/) 
to lint and install Helm charts in a Kubernetes-in-Docker cluster.

It detects which charts have changed and only tests those.

## 🛠 Inputs

| Name         | Description                                                  | Required |
|--------------|--------------------------------------------------------------|----------|
| `chartDirs`  | Comma-separated list of root directories with Helm charts.   | ✅ Yes     |

## 📤 Outputs

| Name     | Description                          |
|----------|--------------------------------------|
| `changed`| Whether any charts were changed.     |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Lint and Test Charts
  uses: MapColonies/shared-workflows/actions/helm-lint@helm-lint-v1.0.0
  with:
    chartDirs: infra/monitoring,infra/sftpgo
```
<!-- x-release-please-end-version -->
