
export interface Tag {

  label: string;

}

export interface FrontMatter {

  title: string;

  description: string;

  published: string;

  tags: string[] | undefined;

  partOf: string[] | undefined;

  /**
   * Link to an associated theses.
   */
  theses: string[] | undefined;

  /**
   * If true the project is not available for students.
   */
  isUnavailable: boolean | undefined;

}

export const TAG_NOT_AVAILABLE = "not-available";

export const TAG_BACHELOR_THESIS = "bachelor-thesis";

export const TAG_MASTER_THESIS = "master-thesis";

export const TAG_PROJECT_IDEA = "project-idea";

const TAGS: Record<string, Tag> = {
  [TAG_BACHELOR_THESIS]: {
    label: "Bachelor thesis",
  },
  [TAG_NOT_AVAILABLE]: {
    label: "Not available",
  },
  [TAG_PROJECT_IDEA]: {
    label: "Project idea",
  },
  [TAG_MASTER_THESIS]: {
    label: "Master thesis",
  },
};

export function isAvailableProject(identifiers: string[]): boolean {
  return !identifiers.includes(TAG_NOT_AVAILABLE) && isProject(identifiers);
}

export function isProject(identifiers: string[]): boolean {
  return identifiers.includes(TAG_BACHELOR_THESIS) ||
    identifiers.includes(TAG_MASTER_THESIS) ||
    identifiers.includes(TAG_PROJECT_IDEA);
}

export function resolveTag(identifier: string): Tag | null {
  return TAGS[identifier] ?? null;
}
