
from github import Github

# Get the GitHub token from the environment variable
token = os.environ['GITHUB_TOKEN']
g = Github(token)

# Replace with your own message content
message = "Hello contributors! Thank you for your contributions."

# Get the repository and create a comment on a specific pull request
repo = g.get_repo("CodeYacht/face-detector.git")
pull_request = repo.get_pull(1)  # Replace 1 with the PR number
pull_request.create_issue_comment(message)

