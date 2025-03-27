#!/bin/bash
cd $SCOPE
git config --global user.name "mapcolonies[bot]"
git config --global user.email "devops[bot]@mapcolonies.com"

git add .
# Add "|| true" for not failing on this line 1
git commit -m "chore: update artifacts.json for $SCOPE" -m "with $TYPE artifact: $ARTIFACT_NAME:$ARTIFACT_TAG" || true

success=false
for ((i=1; i<=5; i++)); do
  echo "Attempt number $i"
  if GIT_ASKPASS=echo git push https://x-access-token:$GITHUB_TOKEN@github.com/$GITHUB_REPOSITORY.git; then
    success=true
    break
  else
    sleep 5
    # --ff for fast-forward
    git pull origin master --ff
  fi
done

if [ "$success" = false ]; then
  echo "Failed to push changes."
  exit 1
fi
