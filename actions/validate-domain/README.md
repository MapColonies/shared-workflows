# validate-domain

Validate that a Helm chart (`Chart.yaml`) contains an `annotations.domain` value that is one of a configured set of allowed domains.

## ✨ What It Does

The action:
Checks if the `Chart.yaml` has the "domain" annotation and validates that the domain is in the domains list

## Inputs

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `chart-file` | no | `helm/Chart.yaml` | Path to the Helm chart file whose `annotations.domain` will be validated. |

The set of allowed domains is constant (not configurable):

```
raster, vector, infra, 3d, app, dem, common
```

If you need to change or extend this list, update the action source or open a PR.


## 🚀 Usage

```yaml
      - name: Validate domain
        uses: MapColonies/shared-workflows/actions/validate-domain@v1
```
