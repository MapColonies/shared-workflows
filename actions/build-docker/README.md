# Build Docker Image Action

This GitHub Action builds a Docker image from a specified context and outputs useful image information for downstream steps

## 🛠 Inputs

| Name         | Description                                                                 | Required | Default                |
|--------------|-----------------------------------------------------------------------------|----------|------------------------|
| `context`    | Path to the Docker build context                                            | ❌ No       | `.`                    |
| `repository` | Repository name for the Docker image (defaults to current GitHub repository)| ❌ No       | `${{ github.repository }}` |
| `domain`     | The image's domain (e.g. `3d`, `infra`).                                    | ✅ Yes      | —                      |
| `registry`   | Azure Registry to authenticate against (e.g. ACR address).                  | ✅ Yes      | —                      |
| `tag`        | Tag for the Docker image                                                    | ❌ No       | `${{ github.ref_name }}`   |

## 📤 Outputs

| Name                   | Description                                      |
|------------------------|--------------------------------------------------|
| `docker_image_name`    | The name of the Docker image (repository name)   |
| `docker_image_tag`     | The version/tag of the Docker image              |
| `docker_image_full_name` | The full name of the Docker image (including registry, domain, and repository) |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Artifactory Login
  uses: MapColonies/shared-workflows/actions/artifactory-login@9a05fd7a01e18746d69cc210b7e6defbd1cc79fc # v1.1.0
  with:
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}

- name: Build Docker Image
  uses: MapColonies/shared-workflows/actions/build-docker@build-docker-v1.1.0
  with:
    domain: infra
    registry: ${{ secrets.ACR_URL }}
```
<!-- x-release-please-end-version -->

---

**Notes:**
- The `docker_image_name` output is just the repository name (e.g., `my-repo`).
- The `docker_image_full_name` output is the full image name including registry, domain, and repository (e.g., `myregistry.azurecr.io/infra/my-repo`).
- Use the outputs in downstream steps, such as for pushing the image.
