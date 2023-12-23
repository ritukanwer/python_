
import requests

# def find_repos_names(username):
#     access_token = "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"
#     url = f"https://api.github.com/users/{username}/repos"
#     headers = {
#         "authorization" : f"token{access_token}"
#     }
#     response = requests.get(url,headers=headers)
#     my_data = response.json()
#     # print(my_data)
#     data_list = []
#     for i in my_data:
#         repo_name = i['name']
#         data_list.append(repo_name)
#
#     return data_list
# print(find_repos_names(username = "ritukanwer"))


def find_commits(username):
    access_token = "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"
    repository = "python_"
    url = f"https://api.github.com/repos/{username}/{repository}/commits"
    headers = {
        "authorozition" : f"token{access_token}"
        }
    total_commit = 0
    commit_list = []

    per_page = 200
    for page in range(1,5):
        response = requests.get(url, headers=headers,params = {"page":page,"per_page":per_page})
        my_data = response.json()
        if len(my_data) > 0:
            total_commit += len(my_data)
    # print(my_data)

            for commits in my_data:
                commits_dict = {"sha":commits['sha'],
                                "name":commits['commit']['author']['name'],
                                "commited_files":commits['commit']['message']}
                commit_list.append(commits_dict)

    return commit_list



a=find_commits(username="ritukanwer")
print(a)
print(len(a))






