# Build and Push Helm Chart Action

This GitHub Action packages a Helm chart and pushes it to a Azure Container Registry.

## 🛠 Inputs

| Name         | Description                                                                                   | Required | Default                |
|--------------|-----------------------------------------------------------------------------------------------|----------|------------------------|
| `domain`      | The chart's domain (e.g. `3d`, `infra`).                      | ✅ Yes   |                    |
| `context`    | Relative path to the Helm chart directory                                                     | ❌ No   | `./helm`               |
| `registry`   | OCI registry URL where the chart will be pushed (e.g. ACR address)                            | ✅ Yes   |                       |


## 📤 Outputs

| Name    | Description                      |
|---------|----------------------------------|
| `chart` | Name of the Helm chart           |
| `ver`   | Version of the Helm chart        |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Artifactory Login
  uses: MapColonies/shared-workflows/actions/artifactory-login@artifactory-login-v2.0.0
  with:
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}

- name: Build and Push Helm Chart
  uses: MapColonies/shared-workflows/actions/build-and-push-helm@build-and-push-helm-v2.0.0
  with:
    context: ./infra/monitoring
    domain: infra
    registry: ${{ secrets.ACR_URL }}
```
<!-- x-release-please-end-version -->
