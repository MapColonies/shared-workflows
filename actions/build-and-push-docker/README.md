# Build and Push Docker Image Action

This GitHub Action builds a Docker image from a specified context and pushes it to a given container registry.

## 🛠 Inputs

| Name         | Description                                                 | Required |
|--------------|-------------------------------------------------------------|----------|
| `context`    | Path to the Docker build context (e.g. `.` or `./app`).     | ✅ Yes   |
| `repository` | Full repository path for the Docker image.                  | ✅ Yes   |
| `scope`      | Scope or namespace for the image (e.g. team/project name).  | ✅ Yes   |
| `registry`   | Container registry URL (e.g. ACR address, etc.).            | ✅ Yes   |


## 🚀 Usage

```yaml
- name: Artifactory Login
  uses: MapColonies/shared-workflows/actions/artifactory-login@artifactory-login-v1
  with:
    registry: ${{ secrets.ACR_URL }}
    username: ${{ secrets.ACR_PUSH_USER }}
    password: ${{ secrets.ACR_PUSH_TOKEN }}

- name: Build and Push Docker Image
  uses: MapColonies/shared-workflows/actions/build-and-push-docker@build-and-push-docker-v1
  with:
    context: .
    scope: infra
    registry: ${{ secrets.ACR_URL }}
    repository: MapColonies/infra-apps
```
