# Push Docker Image Action

This GitHub Action pushes a pre-built Docker image to a container registry.

It is intended to be used **after building an image** using another action like [`build-docker`](../build-docker/).
This action assumes the image is already tagged and available in the local Docker cache.

---

## 🛠 Inputs

| Name         | Description                                        | Required |
|--------------|----------------------------------------------------|----------|
| `image_name` | The fully qualified name of the Docker image (including tag) to push, e.g. `my-registry.com/my-scope/my-image:tag` | ✅ Yes   |

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
        uses: MapColonies/shared-workflows/actions/artifactory-login@artifactory-login-v1.0.0
        with:
          registry: ${{ secrets.ACR_URL }}
          username: ${{ secrets.ACR_PUSH_USER }}
          password: ${{ secrets.ACR_PUSH_TOKEN }}

      - name: Build Docker Image
        id: build
        uses: MapColonies/shared-workflows/actions/build-docker@build-docker-v1.0.0
        with:
          context: ./test
          scope: infra
          registry: ${{ secrets.ACR_URL }}

      - name: Push Docker Image
        uses: MapColonies/shared-workflows/actions/push-docker@push-docker-v1.0.0
        with:
          image_name: $DOCKER_IMAGE_NAME
```
<!-- x-release-please-end-version -->
