# Push Docker Image Action

This GitHub Action pushes a pre-built Docker image to a container registry.

It is intended to be used **after building an image** using another action like [`build-docker`](../build-docker/).
This action assumes the image is already tagged and available in the local Docker cache.

---

## 🛠 Inputs

| Name         | Description                                                                                       | Required | Default  |
|--------------|---------------------------------------------------------------------------------------------------|----------|----------|
| `image_name` | The name of the Docker image to push, including the registry and repository (e.g., `myregistry.azurecr.io/myrepo/myimage`) | ✅ Yes   |          |
| `image_tag`  | Tag of the Docker image to push                                                                   | ❌ No    | `latest` |

---

## 🚀 Usage Example

<!-- x-release-please-start-version -->

```yaml
jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Login to Registry
        uses: MapColonies/shared-workflows/actions/artifactory-login@9a05fd7a01e18746d69cc210b7e6defbd1cc79fc # v1.0.0
        with:
          registry: ${{ secrets.ACR_URL }}
          username: ${{ secrets.ACR_PUSH_USER }}
          password: ${{ secrets.ACR_PUSH_TOKEN }}

      - name: Build Docker Image
        id: build
        uses: MapColonies/shared-workflows/actions/build-docker@e7220d24b1c7ee5c8eaac7e50edc60239e829eb4 # v1.0.0
        with:
          context: ./test
          domain: infra
          registry: ${{ secrets.ACR_URL }}

      - name: Push Docker Image
        uses: MapColonies/shared-workflows/actions/push-docker@push-docker-v1.0.0
        with:
          image_name: ${{ steps.build.outputs.docker_image_name }}
          image_tag: ${{ steps.build.outputs.docker_image_tag }}
```
<!-- x-release-please-end-version -->
