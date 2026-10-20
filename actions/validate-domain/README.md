# validate-domain

Validate that one or more Helm charts (`Chart.yaml`) contain an `annotations.domain` value that is one of a configured set of allowed domains.

## ✨ What It Does

The action:
Checks that each given `Chart.yaml` has the "domain" annotation and that the domain is in the domains list. All charts are checked in one step and every invalid chart is reported.

## Inputs

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `chart-file` | no | `helm/Chart.yaml` | Path to a `Chart.yaml`, or several whitespace-separated paths/globs (e.g. `charts/*/Chart.yaml`). A glob that matches nothing fails. |

The set of allowed domains is constant (not configurable):

```
raster, vector, infra, 3d, app, dem, common
```

If you need to change or extend this list, update the action source or open a PR.

Requires `yq` v4 on the runner (preinstalled on GitHub-hosted Ubuntu runners).


## 🚀 Usage

<!-- x-release-please-start-version -->
```yaml
      - name: Validate domain
        uses: MapColonies/shared-workflows/actions/validate-domain@v1
```
<!-- x-release-please-end-version -->

Validate every chart in a monorepo in one job:

```yaml
      - name: Validate domains
        uses: MapColonies/shared-workflows/actions/validate-domain@v1
        with:
          chart-file: charts/*/Chart.yaml
```
