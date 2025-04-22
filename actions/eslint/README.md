# Run ESLint Action

This GitHub Action installs dependencies and runs ESLint to lint your project codebase.

## 🛠 Inputs

| Name           | Description                           | Default | Required |
|----------------|---------------------------------------|---------|----------|
| `node_version` | Node.js version to set up             | `20`    | false    |
| `path`         | Path to the directory containing your Node.js project| `.`     | false    |

## 🚀 Usage

<!-- x-release-please-start-version -->

```yaml
- name: Run ESLint
  uses: MapColonies/shared-workflows/actions/eslint@eslint-v1.0.0
  with:
    path: ./test
```
<!-- x-release-please-end-version -->
