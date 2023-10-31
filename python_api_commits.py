

import requests
def find_my_all_commits(username):
    access_token = "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"
    repository = "python_"

    url = f"https://api.github.com/repos/{username}/{repository}/commits?page=1 & per_page = 100"
    headers = {"authontication": f"token{access_token}"}
    response = requests.get(url, headers=headers)
    my_data = response.json()

    print(my_data)
    commit_list = []

    for commit in my_data:

        commit_dict = {"commited_name" : commit['commit']['message'],
                      "node_id" : commit['node_id']
                   }
        commit_list.append(commit_dict)

    # page += 1

    return commit_list


my_output = find_my_all_commits(username = "ritukanwer")
print(my_output)
print(len(my_output))
