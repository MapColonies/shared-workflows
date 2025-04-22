# Build Docker Image Action

This GitHub Action builds a Docker image from a specified context

## 🛠 Inputs

| Name         | Description                                                                 | Required | Default                        |
|--------------|-----------------------------------------------------------------------------|----------|--------------------------------|
| `context`    | Path to the Docker build context (e.g. `.` or `./app`).                     | ✅ Yes   | —                              |
| `repository` | Full GitHub repository name. Used for image name.                           | ❌ No    | `${{ github.repository }}`     |
| `domain`      | The image's domain (e.g. `3d`, `infra`).                                 | ✅ Yes   | —                              |
| `registry`   | Registry URL (e.g. ACR address).                                            | ✅ Yes   | —                              |
## 📤 Outputs

| Name    | Description                      |
|---------|----------------------------------|
| `DOCKER_IMAGE_NAME` | Fully qualified Docker image name to push (github output)|

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Artifactory Login
  uses: MapColonies/shared-workflows/actions/artifactory-login@artifactory-login-v1.0.0
  with:
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}

- name: Build Docker Image
  uses: MapColonies/shared-workflows/actions/build-docker@build-docker-v1.0.0
  with:
    context: .
    domain: infra
    registry: ${{ secrets.ACR_URL }}
```
<!-- x-release-please-end-version -->
