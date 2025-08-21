import { type FrontMatter, type Tag, resolveTag } from "../data-model";

export function prepareTags(frontMatter: FrontMatter): Tag[] {
  return (frontMatter.tags ?? [])
    .map(resolveTag)
    .filter(item => item !== null);
}
