# validate-domain

Validate that a Helm chart (`Chart.yaml`) contains an `annotations.domain` value that is one of a configured set of allowed domains.

## ✨ What It Does

The action:
- Reads `.annotations.domain` from the chart using `yq`.
- Splits the `allowed-domains` input on commas only.
- Fails the job if the domain value is not an exact match for one of the allowed items.

## Inputs

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `chart-file` | no | `helm/Chart.yaml` | Path to the Helm chart file whose `annotations.domain` will be validated. |
| `allowed-domains` | no | `raster,vector,infra,3d,app,dem,common` | Comma-separated list of allowed domain values. |


## 🚀 Usage

```yaml
      - name: Validate with custom domains
        uses: MapColonies/shared-workflows/actions/validate-domain@v1
```
