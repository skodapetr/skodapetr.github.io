import rss from "@astrojs/rss";
import { getCollection } from "astro:content";

export async function GET(context) {
	const posts = await getCollection("post");
	return rss({
		title: "Škoda Petr",
		description: "My personal website.",
		site: context.site,
		items: posts.map((post) => ({
			...post.data,
			pubDate: post.data.published,
			link: `/post/${post.slug}/`,
		})),
	});
}
