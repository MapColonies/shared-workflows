#!/bin/bash
ARTIFACTS_PATH="$TARGET_DIR/$DOMAIN/artifacts.json"

# Make sure the directory exists
mkdir -p "$(dirname "$ARTIFACTS_PATH")"

# If the file doesn't exist, initialize it
[[ -f "$ARTIFACTS_PATH" ]] || echo '{}' > "$ARTIFACTS_PATH"

# Ensure nested structure and assign artifact tag
tmp_file=$(mktemp)
jq --arg type "$TYPE" \
   --arg registry "$REGISTRY" \
   --arg key "${DOMAIN}/${ARTIFACT_NAME}" \
   --arg tag "$ARTIFACT_TAG" '
   .[$type] += {} | 
   .[$type][$registry] += {} | 
   .[$type][$registry][$key] = $tag
' "$ARTIFACTS_PATH" > "$tmp_file" && mv "$tmp_file" "$ARTIFACTS_PATH"

echo "artifacts.json updated successfully at $ARTIFACTS_PATH"
