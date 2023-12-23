
import requests
def find_my_all_commits(username):
    access_token = "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"
    repository = "python_"

    url = f"https://api.github.com/repos/{username}/{repository}/commits"
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
