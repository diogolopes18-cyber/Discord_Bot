import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.getenv("APP_KEY")
APP_ID = os.getenv("APP_ID")
API_URL = os.getenv("API_URL")


class JobSearchResult:
    def __init__(self, title, company, location, contract_time, url):
        self.title = title
        self.company = company
        self.location = location
        self.contract_time = contract_time
        self.url = url
        self.description = description

    def format_result(self):
        jobs = {
            "Job Title": self.title,
            "Company": self.company,
            "Location": self.location,
            "Type": self.contract_time,
            "Url": self.url
        }

        return jobs


class SearchJobs:
    def __init__(self, country=None, role=None):
        self.country = country
        self.role = role
        self.api_url = API_URL
        self.app_id = APP_ID
        self.app_key = APP_KEY

    def search_jobs_by_country(self):
        # Sets the request to accept JSON responses
        headers = {
            "Accept": "application/json"
        }

        params = {
            "app_id": self.app_id,
            "app_key": self.app_key
        }

        # Searches for a specific role
        if self.role is not None:
            params = {
                "app_id": self.app_id,
                "app_key": self.app_key,
                "what": self.role
            }

        if self.country is not None:
            return requests.get(url=self.api_url.replace("gb", self.country),
                                headers=headers, params=params).json()

        return requests.get(url=self.api_url, headers=headers, params=params).json()

    def format_job_search(self):
        formatted_result = list()
        result = self.search_jobs_by_country()

        # Define list of attributes for the selected job
        for i in range(0, 10):
            formatted_jobs = JobSearchResult(result["results"][i]["title"],
                                             result["results"][i]["salary_min"],
                                             result["results"][i]["contract_time"],
                                             result["results"][i]["redirect_url"],
                                             result["results"][i]["description"]).format_result()

            formatted_result.append(formatted_jobs)

        return formatted_result

