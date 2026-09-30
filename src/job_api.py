# Fetch 20 Linkedin Jobs based of the search_query and location
import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()
apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))


def fetch_linkedin_jobs(search_query, location="india", rows=20):

    run_input = {
        "title": search_query,
        "location": location,
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        }
    }

    # Execute Apify actor
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(
        run_input=run_input
    )

    if not run:
        raise RuntimeError("Apify actor did not return a response.")

    # Access Run object using attributes
    print("Actor status:", run.status)
    print("Dataset ID:", run.default_dataset_id)

    # Check actor status
    if run.status != "SUCCEEDED":
        raise RuntimeError(
            f"Apify actor failed. Status: {run.status}"
        )

    # Get dataset ID
    dataset_id = run.default_dataset_id

    if not dataset_id:
        raise RuntimeError("Apify did not return a dataset ID.")

    # Fetch jobs from dataset
    jobs = list(
        apify_client.dataset(dataset_id).iterate_items()
    )

    print(f"Total LinkedIn jobs fetched: {len(jobs)}")

    return jobs



# Fetch 20 Naukari Jobs based of the search_query and location
def fetch_naukari_jobs(search_query, location="india", rows=20):

    run_input = {
        "keyword": search_query,
        "maxJobs": max(50, rows),
        "sortBy": "relevance",
        "experience": "all",
        "freshness": "all"
    }

    run = apify_client.actor("alpcnRV9YI9lYVPWk").call(
        run_input=run_input
    )

    if not run:
        raise RuntimeError("Apify Naukri actor did not return a response.")

    print("Actor status:", run.status)
    print("Dataset ID:", run.default_dataset_id)

    if run.status != "SUCCEEDED":
        raise RuntimeError(
            f"Naukri actor failed. Status: {run.status}"
        )

    dataset_id = run.default_dataset_id

    if not dataset_id:
        raise RuntimeError("Naukri actor did not return a dataset ID.")

    jobs = list(
        apify_client.dataset(dataset_id).iterate_items()
    )

    print(f"Total Naukri jobs fetched: {len(jobs)}")

    return jobs
