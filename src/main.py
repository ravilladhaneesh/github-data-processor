import os
import datetime
import github_api as git_api
import process_repo


print('----------------------')
print('TEST GITHUB ACTIONS')
print('----------------------')

repo_name = os.environ.get('REPO_NAME')
repo_path = os.environ.get('REPO_PATH')
branch = os.environ.get('BRANCH')
repo_url = os.environ.get('REPO_URL')
repo_visibility = os.environ.get('REPO_VISIBILITY')
now = datetime.datetime.now()

#local
'''
repo_name = 'ravilladhaneesh/github-viewer'
repo_path = os.getcwd()
branch = 'dummy'
repo_url = 'https://github.com/ravilladhaneesh/github-viewer'
repo_visibility = True
'''



print(f"repo name: {repo_name}")
print('---------------------')
print(f'repo path: {repo_path}')
print('---------------------')
print(f'repo url: {repo_url}')
print('---------------------')
print(f'branch: {branch}')
print('---------------------')
print(f'visibility: {repo_visibility}')
print('---------------------')
print(f'current time: {now}')
print('---------------------')


"""
Function that processes the repo and gets the repo data
"""
def get_repo_data(name, branch, url, path):

    default_branches = {'master', 'main'}
    
    if branch in default_branches:
        languages_data = git_api.get_languages(name)
    else:
        languages_data = process_repo.get_files_of_non_default_branch(name, path)

    languages_percentage = process_repo.get_languages_percentage(languages_data)
    map_language_names = process_repo.get_languages(languages_percentage)
    print(map_language_names)



get_repo_data(repo_name, branch, repo_url, repo_path)