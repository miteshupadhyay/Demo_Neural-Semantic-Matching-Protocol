from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_naukari_jobs, fetch_linkedin_jobs

mcp = FastMCP("Job Search MCP Server")


@mcp.tool()
async def fetchlinkedin(listofkey: list[str]):
    """Fetch LinkedIn jobs using the provided search keywords."""
    return fetch_linkedin_jobs(listofkey)


@mcp.tool()
async def fetchnaukari(listofkey: list[str]):
    """Fetch Naukri jobs using the provided search keywords."""
    return fetch_naukari_jobs(listofkey)


if __name__ == "__main__":
    mcp.run(transport="stdio")
