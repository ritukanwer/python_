
import requests
def find_my_all_commits(username):
    access_token = "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"

    repository = "python_"

    url = f"https://api.github.com/repos/{username}/{repository}/commits"

    headers = {"authorozition": f"token{access_token}"}

    commit_list = []
    total_commit = 0
    # page = 1
    per_page = 200
    for page in range(1,5):
        response = requests.get(url, headers=headers, params={"page": page, "per_page": per_page})
        my_data = response.json()
        # print(my_data)
        if len(my_data) > 0:
            total_commit += len(my_data)
            # print(total_commit)
            for commit in my_data:
                commit_dict = {"commited_name" : commit['commit']['message'],
                                  "node_id" : commit['node_id']
                               }
                commit_list.append(commit_dict)
    return commit_list


my_output = find_my_all_commits(username = "ritukanwer")
print(my_output)
print(len(my_output))