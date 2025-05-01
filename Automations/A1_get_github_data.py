import requests
import os 

# Need to use token if we want to fetch private repo.
# GITHUB_TOKEN= os.getenv("GITHUB_TOKEN")
# GITHUB_USERNAME = "kaushal-hirani"


owner = "kaushal-hirani"
repo = "Devops-Assignments"

# GitHub API URL for the repo
url = f"https://api.github.com/repos/{owner}/{repo}"

# Make the request without authentication
response = requests.get(url)

# Handle the response
if response.status_code == 200:
    repo = response.json()
    print("📦 Repository Name:", repo["name"])
    print("🔓 Public Repo")
    print("📝 Description:", repo.get("description", "No description"))
    print("⭐ Stars:", repo["stargazers_count"])
    print("🍴 Forks:", repo["forks_count"])
    print("👀 Visibility:", repo["visibility"])
    print("📅 Created At:", repo["created_at"])
    print("🔄 Last Push:", repo["pushed_at"])
else:
    print("❌ Failed to fetch repo.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)