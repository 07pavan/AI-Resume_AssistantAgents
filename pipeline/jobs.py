import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")


def suggest_jobs(query):

    # Check API key
    if not API_KEY:
        return "⚠️ RapidAPI key not configured."

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "num_pages": "1"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        # Handle API limit
        if response.status_code == 429:
            return "⚠️ Job API rate limit reached. Please try again later."

        # Handle other API errors
        if response.status_code != 200:
            return f"⚠️ Job API error (status {response.status_code})."

        try:
            data = response.json()
        except ValueError:
            return "⚠️ Invalid response from Job API."

        if not data or "data" not in data:
            return "⚠️ Unexpected API response."

        job_data = data["data"]

        if not job_data:
            return "⚠️ No jobs found for this role."

        jobs = []

        for job in job_data[:5]:

            title = job.get("job_title", "Unknown Role")
            company = job.get("employer_name", "Unknown Company")
            location = job.get("job_city") or job.get("job_country") or "Unknown Location"
            link = job.get("job_apply_link") or "#"

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link
            })

        return jobs

    except requests.exceptions.Timeout:
        return "⚠️ Job API request timed out."

    except requests.exceptions.ConnectionError:
        return "⚠️ Unable to connect to Job API."

    except Exception as e:
        return f"⚠️ Unexpected Job API error: {str(e)}"