export function addTagToSelected(tag, selectedTags) {
  if (selectedTags.value.length > 3) {
    return;
  } else if (!tag.value) return;
  selectedTags.value.push(tag.value);
  tag.value = "";
}
export function removeTagFromSelected(key, selectedTags) {
  selectedTags.value = selectedTags.value.filter((tag, index) => index !== key);
}
