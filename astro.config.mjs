import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import yaml from "@rollup/plugin-yaml";

import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
	base: "/",
	site: "https://skodapetr.github.io/",
	integrations: [mdx(), sitemap()],
	devToolbar: {
		enabled: false
	},
	vite: {
    plugins: [yaml()]
  }
});
