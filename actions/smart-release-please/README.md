# Smart Release Please Action

This GitHub Action is a wrapper around [googleapis/release-please-action](https://github.com/googleapis/release-please-action). It's designed to enforce a specific versioning strategy for release candidates (RCs) on the `next` branch.

When commits on the `next` branch consist only of `fix`, `chore`, or other non-`feat` types, this action ensures that `release-please` increments the RC number (e.g., `v1.2.3-rc.1` -> `v1.2.3-rc.2`) instead of incorrectly creating a new minor version release.

It achieves this by:
1.  Analyzing the commit history since the last `rc` tag on the `next` branch.
2.  Calculating the correct semantic version for the next RC.
3.  Creating an empty commit with a `Release-As: <version>` footer, which instructs `release-please` to use that specific version.

This action is intended to be used on pushes to the `next` branch.

## 🛠 Inputs

| Name    | Description                                                       | Required | Default            |
|---------|-------------------------------------------------------------------|----------|--------------------|
| `token` | GitHub Token (PAT) for pushing commits and triggering releases. It can be passed in order to trigger workflows after this one  | No       | `${{ github.token }}` |


## 🚀 Usage

```yaml
name: Release Next

on:
  push:
    branches:
      - next

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: MapColonies/shared-workflows/actions/smart-release-please@main
        with:
          token: ${{ secrets.PAT_TOKEN }} # A PAT is required for the subsequent workflow to be triggered
```
