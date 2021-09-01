# API Requests - Gitlab using http request/response
# Simple project List
# remote app is gitlab
# ref; https://docs.gitlab.com/ee/api/
# base url https://gitlab.com/api/v4/users/usr_id:/projects
# Local python app
#
import requests

response = requests.get("https://gitlab.com/api/v4/users/your_gitlab_usr_id:/projects")
print(response)

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']} Project Url: {project['web_url']} \n")

