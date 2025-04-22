# OpenAPI Lint Action

This GitHub Action installs Node.js dependencies, runs code linting, and validates an OpenAPI specification using Redocly CLI.


## 🛠 Inputs

| Name           | Description                           | Default | Required |
|----------------|---------------------------------------|---------|----------|
| `node_version` | Node.js version to set up             | `20`    | ❌ No	    |
| `path`         | Path to the directory containing your Node.js project| `.`     | ❌ No	    |
| `openapi-file` | Path to the OpenAPI file (e.g. ./openapi3.yaml)	| `.` | ❌ No	 |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Run OpenAPI Lint
  uses: MapColonies/shared-workflows/actions/openapi-lint@openapi-lint-v1.0.0
  with:
    node_version: "20"
    openapi-file: "./openapi3.yaml"
    path: "."

```
<!-- x-release-please-end-version -->
