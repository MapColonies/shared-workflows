# Initialize NPM Action

This GitHub Action sets up Node.js, installs dependencies using npm, and builds the project.

## 🛠 Inputs

| Name           | Description                           | Default | Required |
|----------------|---------------------------------------|---------|----------|
| `node_version` | Node.js version to set up ([supported versions](https://github.com/actions/setup-node#supported-version-syntax))      | `22.x`  | false    |
| `path` | Path to the directory containing your Node.js project             | `.`  | false    |

## 🚀 Usage

<!-- x-release-please-start-version -->
```yaml
- name: Initialize NPM Project
  uses: MapColonies/shared-workflows/actions/init-npm@init-npm-v1.0.0
  with:
    node-version: '22.x'
```
<!-- x-release-please-end-version -->
