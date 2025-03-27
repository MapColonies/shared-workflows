# 📦 Publish npm Package Action

This GitHub Action installs dependencies, runs a `prepack` script, and publishes a package to the npm registry using
[`npm-publish`](https://github.com/JS-DevTools/npm-publish).

---

## 🛠 Inputs

| Name           | Description                              | Required | Default                           |
|----------------|------------------------------------------|----------|-----------------------------------|
| `node-version` | The version of Node.js to use            | ✅ Yes   | `20`                              |
| `npm-token`    | npm authentication token (`NODE_AUTH_TOKEN`) | ✅ Yes   | —                                 |
| `repository`   | GitHub repository to checkout            | ✅ Yes   | `${{ github.action_repository }}` |

---

## 🚀 Usage

```yaml
- name: Publish npm Package
  uses: MapColonies/shared-workflows/actions/publish-npm@v1
  with:
    node-version: '20'
    npm-token: ${{ secrets.NPM_TOKEN }}
    repository: MapColonies/infra-portal
```
