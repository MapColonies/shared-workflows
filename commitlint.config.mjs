export default {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "scope-empty": [1, "never"],
    "scope-enum": [
      2,
      "always",
      [
        "repo",
        "commitlint",
        "pull-request",
        "npm-publish",
        "push-docker",
        "push-helm",
        "update-artifacts",
      ],
    ],
    "header-min-length": [2, "always", 10],
  },
};
