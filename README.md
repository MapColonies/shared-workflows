# ⚙️ MapColonies Shared GitHub Actions

This repository contains GitHub Actions used across the MapColonies organization, developed and maintained by the **DevOps team**.

> 🧪 The workflows in this repo are primarily for testing and validating the functionality of these actions — **not for general use** in other projects, unless stated otherwise.

---

## 📂 Structure

```
.
├── actions/                # Reusable composite actions
│   ├── build-and-push-helm/
│   ├── helm-lint/
│   ├── init-npm/
│   └── update-artifacts-file/
├── test/                   # Assets for testing the actions
├── .github/workflows/      # Utility and Test workflows for each action
├── release-please-config.json
└── README.md
```

Each action has a dedicated folder with:
- `action.yaml` – definition of the action
- `README.md` – usage and inputs specific to the action

---

## 🧪 Purpose of This Repo

- Maintain reusable actions for use in other repositories
- Create test workflows to verify action behavior before tagging
- Manage action versioning and changelogs via `release-please`
- Provide general-use workflows like slash-command triggers

---

## 📦 Actions Included

| Action | Description |
|--------|-------------|
| `build-and-push-helm`     | Packages and publishes Helm charts |
| `helm-lint`               | Lints and tests Helm charts |
| `init-npm`                | Initializes the repo with npm |
| `update-artifacts-file`   | Updates `artifacts.json` metadata |

---

## 🧰 Public Workflows

| Workflow        | Purpose                                        |
|----------------|------------------------------------------------|
| `slash-command`| Dispatch slash-command triggered workflows     |
| `postgis-check`| Test DB migrations and compatibility via PR comments |

### slash-command

The slash-command workflow enables users to trigger workflows by commenting commands such as /postgis-check on pull requests or issues.
It listens for new comments, detects if a command matches a preconfigured list, and dispatches the corresponding workflow using GitHub’s workflow_call event.
It passes essential metadata — like the pull request’s latest commit SHA, the comment timestamp, and the issue number — to the triggered workflow.

If the command is invalid or dispatching fails, the workflow uses the peter-evans/create-or-update-comment 
action to post a detailed error comment back to the thread. This provides contributors and maintainers an easy
way to trigger validation workflows on demand without pushing new code or rerunning entire CI pipelines.
 
| Input        | Description                                        |
|----------------|------------------------------------------------|
| `head-sha`| The SHA of the commit to run the triggered workflow against (usually from the PR head) |

### postgis-check
The postgis-check workflow is designed to verify database migrations and application compatibility across a matrix of PostgreSQL + PostGIS and Node.js versions. It's particularly useful for repositories with spatial data handling and migration scripts.

When triggered (often via a slash command), the workflow first checks for supplied inputs like PostGIS versions and Node.js versions.
It then generates a matrix of all combinations to test. For each combination, it sets up a Docker container running the specified PostGIS version,
installs Node.js, installs dependencies, creates the target schema in the database, runs migration scripts, and executes integration tests.

After the tests run, the workflow finds the original slash command comment in the PR thread and posts an update using the appropriate ✅ or ❌ emoji
to indicate success or failure.

| Input        | Description                                       |
|----------------|------------------------------------------------|
| `head-sha` | The SHA to checkout and test                           |
| `issue-number` | The GitHub issue or PR number (used for commenting test results) |
| `comment-creation-date` | The timestamp of the original slash command comment |
| `versions` | (Optional) Comma-separated list of PostGIS versions to test (e.g., 14-3.3,15-3.5) |
| `node-versions` | (Optional) Comma-separated list of Node.js versions to test (default: 20.x) |
| `db-schema` | Schema name to create and apply migrations into |
