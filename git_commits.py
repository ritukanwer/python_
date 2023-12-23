import requests
def get_repos_names(user_name):
    access_token = "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"
    repository = "python_"
    url = f"https://api.github.com/repos/{user_name}/{repository}/commits"
    headers = {
        'Authorization': f'token {access_token}'
    }

    response = requests.get(url, headers=headers)
    my_data = response.json()
    # commit_list = []

    for commit in my_data:
        print(commit)
    #     commit_dict = {
    #         "sha": commit['sha'],
    #         "author_name":commit['commit']['author']['name'],
    #         "date":commit['commit']['author']['date']
    #     }
    #     commit_list.append(commit_dict)
    # return commit_list


print(get_repos_names(user_name = 'ritukanwer'))





