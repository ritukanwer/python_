


import requests
def find_commits(username):
    access_token = "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"
    repository = "python_"
    url = f"https://api.github.com/repos/{username}/{repository}/commits"
    headers = {"authorozition": f"token{access_token}"}
    response = requests.get(url, headers = headers)
    my_data = response.json()
    # print(my_data)
    commit_list = []
    for commit in my_data:
        commit_items = {
            "sha" : commit['sha'],
            "author":commit['commit']['author']['name'],
            "email":commit['commit']['author']['email'],
            "date":commit['commit']['author']['date']

        }
        commit_list.append(commit_items)

    return commit_list
output = find_commits(username = "ritukanwer")
print(output)



