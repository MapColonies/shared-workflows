# Build Docker Image Action

This GitHub Action builds a Docker image from a specified context

## 🛠 Inputs

| Name         | Description                                                                 | Required | Default                |
|--------------|-----------------------------------------------------------------------------|----------|------------------------|
| `context`    | Path to the Docker build context                                            | ❌ No       | `.`                    |
| `repository` | Repository name for the Docker image (defaults to current GitHub repository)| ❌ No       | `${{ github.repository }}` |
| `domain`     | The image's domain (e.g. `3d`, `infra`).                                    | ✅ Yes      | —                      |
| `registry`   | Azure Registry to authenticate against (e.g. ACR address).                  | ✅ Yes      | —                      |
| `tag`        | Tag for the Docker image                                                    | ❌ No       | `${{ github.ref_name }}`   |

## 📤 Outputs

| Name                | Description                                      |
|---------------------|--------------------------------------------------|
| `docker_image_name` | The name of the Docker image                     |
| `docker_image_tag`  | The version/tag of the Docker image              |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Artifactory Login
  uses: MapColonies/shared-workflows/actions/artifactory-login@9a05fd7a01e18746d69cc210b7e6defbd1cc79fc # v1.0.0
  with:
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}

- name: Build Docker Image
  uses: MapColonies/shared-workflows/actions/build-docker@build-docker-v1.0.0
  with:
    domain: infra
    registry: ${{ secrets.ACR_URL }}
```
<!-- x-release-please-end-version -->
