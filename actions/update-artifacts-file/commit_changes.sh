#!/bin/bash
cd "$TARGET_DIR"

git config user.name "mapcolonies[bot]"
git config user.email "devops[bot]@mapcolonies.com"

git checkout "$TARGET_BRANCH"

git add "$DOMAIN/artifacts.json"
git commit -m "chore: update artifacts.json for $DOMAIN" -m "with $TYPE artifact: $ARTIFACT_NAME:$ARTIFACT_TAG" || echo "Nothing to commit"

success=false
for ((i=1; i<=5; i++)); do
  echo "Attempt $i to push changes..."
  if git push https://x-access-token:$GITHUB_TOKEN@github.com/$TARGET_REPO.git "$TARGET_BRANCH"; then
    success=true
    echo "Push succeeded"
    break
  else
    echo "Push failed, retrying after pull"
    git pull origin "$TARGET_BRANCH" --ff-only || true
    sleep 5
  fi
done

if [ "$success" = false ]; then
  echo "Failed to push changes after 5 attempts."
  exit 1
fi
