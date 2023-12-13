

import requests
def find_repo_name(username):
    access_token = "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"
    url = f"https://api.github.com/users/{username}/repos"
    headers = {'authorization' : f'tokan{access_token}'
    }
    response = requests.get(url, headers=headers)
    my_data = response.json()
    # print(my_data)
    repository_name = []
    for commit in my_data:
        repos_name = commit['name']
        repository_name.append(repos_name)

    return repository_name

print(find_repo_name(username = 'ritukanwer'))





