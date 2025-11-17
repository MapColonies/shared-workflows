# validate-domain

Validate that a Helm chart (`Chart.yaml`) contains an `annotations.domain` value that is one of a configured set of allowed domains.

## ✨ What It Does

The action:
Checks if the `Chart.yaml` has the "domain" annotation and validates that the domain is in the domains list

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
