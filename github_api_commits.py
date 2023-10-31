


import requests
def find_my_all_commits(username):
    access_token = "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"

    repository = "python_"

    url = f"https://api.github.com/repos/{username}/{repository}/commits"

    headers = {"authorozition": f"token{access_token}"}
    params = {
        page >= 1, per_page >= 100}
    commit_list = []
    total_commit = 0
    page = 1
    per_page = 100
    if
    for pages in params:
        response = requests.get(url, headers=headers)
        my_data = response.json()
        total_commit += 1
        print(total_commit)


    # print(my_data)

    for commit in my_data:
        commit_dict = {"commited_name" : commit['commit']['message'],
                      "node_id" : commit['node_id']
                   }
        commit_list.append(commit_dict)

    # page += 1

    return total_commit


my_output = find_my_all_commits(username = "ritukanwer")
print(my_output)
# print(len(my_output))
