#!/bin/bash
# Split string by comma
echo "$SCOPE" | tr ',' '\n' | while read -r element; do
  # Check if the directory exists
  if [ -d "$element" ]; then
    path="$element/artifacts.json"
    # Create a default empty JSON if the file doesn't exist
    [[ -f "$path" ]] || echo '{}' > "$path"
    # Ensure nested structure and assign artifact tag
    jq --arg type "$TYPE" \
      --arg registry "$REGISTRY" \
      --arg key "${element}/$ARTIFACT_NAME" \
      --arg tag "$ARTIFACT_TAG" \
      '.[$type][$registry][$key] = $tag' "$path" > tmp.json && mv tmp.json "$path"
  else
    echo "Directory $REPOSITORY/$element does not exist"
  fi
done
