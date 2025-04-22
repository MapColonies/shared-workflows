# Artifactory Login Action

This GitHub Action logs into MapColonies Artifactory (Azure Container Registry) to enable
authenticated operations like pulling or pushing images.

## 🛠 Inputs

| Name      | Description                              | Required |
|-----------|------------------------------------------|----------|
| `registry` | The Artifactory registry URL              | ✅ Yes   |
| `username` | Username for the registry                 | ✅ Yes   |
| `password` | Password or token for the registry        | ✅ Yes   |

## 🚀 Usage

<!-- x-release-please-start-version -->
```yaml
- name: Artifactory Login
  uses: MapColonies/shared-workflows/actions/artifactory-login@artifactory-login-v1.0.0
  with:
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}
```
<!-- x-release-please-end-version -->
