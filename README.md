# shared-workflows

In this repository we can find reusable workflows that can be used from within other repositories in this organization.
Here's the shared workflows we can find in this repository:

## 1. build-and-push-docker
This workflow builds a docker image and and pushes it to the registry.
This workflow also utilizes `update-artifact-file` workflow, to edit the `artifacts.yaml` file in the [common helm charts](https://github.com/mapcolonies/helm-charts/) repository.
### Workflow parameters:
| Name       | Description                                                               | Type   | Required? | Default Value |
|------------|---------------------------------------------------------------------------|--------|-----------|---------------|
| scope         | This is the subdirectory in the helm-charts repository: `helm-charts/<scope>` | string | no       |   ''
| repository | If you want to override default's docker image name                       | string | no        |               |
| context    | From where the CI should build the docker image                           | string | no        | . (Current context)             |

```mermaid
%%{
  init: {
    'theme': 'forest',
    'themeVariables': {
      'lineColor': '#F8B229'
    }
  }
}%%
flowchart TD
    classDef head fill:#5882FA
    classDef workflow fill:#8258FA
    A[Build And Push Docker]:::head --> B[Checkout latest commit]
    B --> C(Login to Remote Registry)
    C --> D(Generate Docker Image Name)
    D --> E( Build Image)
    E --> F[Push Image]
    F --> G[Trigger update-artifacts-file workflow]:::workflow
```

## 2. build-and-push-helm
This workflow package a helm chart and and pushes it to the registry.
This workflow also utilizes `update-artifact-file` workflow, to edit the `artifacts.yaml` file in the [common helm charts](https://github.com/mapcolonies/helm-charts/) repository. 

Helm chart's name and version are inferred automatically from the `Chart.yaml` file.
### Workflow parameters:
| Name       | Description                                                               | Type   | Required? | Default Value |
|------------|---------------------------------------------------------------------------|--------|-----------|---------------|
| scope         | This is the subdirectory in the helm-charts repository: `helm-charts/<scope>` | string | no       |  ''

```mermaid
%%{
  init: {
    'theme': 'forest',
    'themeVariables': {
      'lineColor': '#F8B229'
    }
  }
}%%
flowchart TD
    classDef head fill:#5882FA
    classDef workflow fill:#8258FA
    A[Build And Push Helm]:::head --> B[Checkout latest commit]
    B --> C[Setup Helm]
    C --> D[Login to Remote Registry]
    D --> E(Retrieve Chart Name)
    E --> F[Retrieve Chart Version]
    F --> G[Package Chart into TGZ]
    G --> H[Publish Chart to ACR]
    H --> I[Trigger update-artifacts-file workflow]:::workflow
```

## 3. pull_request
This workflow should be used in your pull requests; here linters run, Snyk checks for vulnerabilities, tests of the service, and a dummy docker build to check that docker image can be still built and hasn't broken.

### Workflow parameters:
| Name               | Description                                              | Type    | Required? | Default Value   |
|--------------------|----------------------------------------------------------|---------|-----------|-----------------|
| enableOpenApiCheck | Flag to enable OpenAPI lint checks                       | boolean | no        | true            |
| openApiFilePath    | Path to the OpenAPI file (if enableOpenApiCheck is true) | string  | no        | ./openapi3.yaml |
| usePostgres    | Flag whether to initiate postgres service or not             | boolean | no        | false           |

```mermaid
%%{
  init: {
    'theme': 'forest',
    'themeVariables': {
      'lineColor': '#F8B229'
    }
  }
}%%
flowchart TD
    classDef parent fill:#f946
    classDef head fill:#5882FA
    A[Pull Request]:::head -->|INPUTS: \n enableOpenApiCheck \n openApiFilePath \n usePostgres| B[Jobs]
    B --> C[ESLint Job]:::parent
    C --> D[Checkout Git repository]
    D --> E[Set up Node.js]
    E --> F[Install dependencies]
    F --> G[Run linters]
    G -->|enableOpenApiCheck==true| H[Lint Checks on OpenAPI File]
    B --> I[Security Job]:::parent
    I --> J[Checkout Git repository]
    J --> K[Run Snyk to check for vulnerabilities]
    B --> L[Tests Job]:::parent
    L -->|usePostgres==true| N[Start Postgres]
    L -->|usePostgres==false| O[Checkout Git repository]
    N --> O
    O --> P[Set up Node.js]
    P --> Q[Install Node.js dependencies]
    Q --> R[Run tests]
    R --> S[Upload Test Reporters]
    B --> T[Build Image Job]:::parent
    T --> U[Checkout Git repository]
    U --> V[Build Docker image]
```

## 4. release-on-tag-push
This workflow creates a release. Its trigger event should be when a new tag is craeted in the repository. This workflow generates postman collection for the service, and modifies the `CHANGELOG.md` file respectively.

### Workflow parameters:
| Name               | Description                                              | Type    | Required? | Default Value   |
|--------------------|----------------------------------------------------------|---------|-----------|-----------------|
| enableOpenApiToPostman | Flag to enable OpenAPI to Postman collection conversion                       | boolean | no        | true            |

```mermaid
%%{
  init: {
    'theme': 'forest',
    'themeVariables': {
      'lineColor': '#F8B229'
    }
  }
}%%
flowchart TD
    classDef head fill:#5882FA
    A[Release On Tag Push]:::head -->|INPUTS: \n enableOpenApiToPostman| C["Checkout Git repository for CHANGELOG.md \n (for release notes)"]
    C --> D[Get package info]
    D --> E["Setup Node.js \n (for postman collection)"]
    E --> F[Set Collection File Name Env]
    F -->|enableOpenApiToPostman==true| G[Add openapi to Postman Collection]
    G --> H[Publish Release to GitHub]
    F --> |else| H
```

## 5. update-artifacts-file
This workflow edits the `artifacts.json` according to the input.

### Workflow parameters:
| Name          | Description                            | Type                                  | Required? | Default Value |
|---------------|----------------------------------------|---------------------------------------|-----------|---------------|
| scope         | This is the subdirectory in the helm-charts repository: `helm-charts/<scope>` | string | no       | ''              |
| type          | Artifact`s type                        | string                                | no        | docker        |
| artifact-name | Artifact`s name                        | string                                | yes       |               |
| artifact-tag  | Aritfact`s tag                         | string                                | yes       |               |

```mermaid
%%{
  init: {
    'theme': 'forest',
    'themeVariables': {
      'lineColor': '#F8B229'
    }
  }
}%%
flowchart TD
    classDef head fill:#5882FA
    A[Edit artifacts.json in helm-charts]:::head -->|INPUTS: \n artifact-name \n artifact-tag| D["Checkout helm-charts Repository \n (access the helm-charts repository for modification)"]
    D --> E[Set up Node.js]
    E -->|using the inputs| F["Modify artifacts.json \n (update artifacts.json with new artifact data)"]
    F --> G["Commit Changes \n (commit and push the updated artifacts.json back to the repository)"]

```
