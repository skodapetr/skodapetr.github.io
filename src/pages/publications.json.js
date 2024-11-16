import publications from "../../data/publications.yaml";

export async function GET() {
  const payload = publications.map(item => ({
    title: item.title,
    doi: item.doi,
    year: item.year,
    journal: item.journal,
  }));

  return new Response(JSON.stringify(payload));
}
