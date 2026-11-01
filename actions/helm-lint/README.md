# Lint and Test Helm Charts Action

This GitHub Action uses [chart-testing (ct)](https://github.com/helm/chart-testing) and [kind](https://kind.sigs.k8s.io/) 
to lint and install Helm charts in a Kubernetes-in-Docker cluster.

It detects which charts have changed and only tests those.

## 🛠 Inputs

| Name         | Description                                                                 | Required |
|--------------|-----------------------------------------------------------------------------|----------|
| `chartPaths` | Comma-separated list of root directories with Helm charts.                  | No       |
| `registry`   | OCI registry to log in to before building chart dependencies.               | No       |
| `username`   | Registry username.                                                          | No       |
| `password`   | Registry password.                                                          | No       |
| `install`    | `true` to also install the changed charts in a kind cluster. Default `false`. | No       |

Lint (and install) run only when `registry`, `username` and `password` are all set, since
`ct lint` builds chart dependencies and most charts depend on charts in the OCI registry.

Lint uses the action's `ct.yaml` (no version-bump or maintainers check) and `lintconf.yaml`
(ct's default, except `brackets`, `comments` and `trailing-spaces` only warn).

## 📤 Outputs

| Name     | Description                          |
|----------|--------------------------------------|
| `changed`| Whether any charts were changed.     |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Lint and Test Charts
  uses: MapColonies/shared-workflows/actions/helm-lint@helm-lint-v1.2.0
  with:
    chartPaths: infra/monitoring,infra/sftpgo
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}
```
<!-- x-release-please-end-version -->
