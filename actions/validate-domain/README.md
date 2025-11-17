# validate-domain

Validate that a Helm Chart (`Chart.yaml`) contains an `annotations.domain` value and that it matches one of the allowed domains.

## Inputs

- `chart-file` (optional): Path to the `Chart.yaml` to validate. Default: `helm/Chart.yaml`.
- `allowed-domains` (optional): Space-separated list of allowed domain values. Default: `raster vector infra 3d app dem common`.

## Usage

```yaml
name: Validate Helm domain annotation

on:
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v5

      - name: Validate Helm annotations.domain
        uses: MapColonies/shared-workflows/actions/validate-domain@v1
        with:
          # Optional overrides
          # chart-file: helm/Chart.yaml
          # allowed-domains: "raster vector infra 3d app dem common"
```

## Behavior

- Fails the job if `.annotations.domain` is missing or equals `null`.
- Fails the job if `.annotations.domain` is not one of the allowed domains.
- Prints a GitHub Actions error annotation pointing to the `Chart.yaml` file on failure.

## Notes

- Ensure the repository is checked out before using this action (use `actions/checkout`).
- This action uses `mikefarah/yq` to read the YAML field.
