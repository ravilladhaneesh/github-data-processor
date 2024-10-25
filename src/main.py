import os
import datetime
import github_api as git_api



print('----------------------')
print('TEST GITHUB ACTIONS')
print('----------------------')

repo_name = os.environ.get('REPO_NAME')
repo_path = os.environ.get('REPO_PATH')
repo_branch = os.environ.get('REPO_BRANCH')
repo_url = os.environ.get('REPO_URL')
repo_visibility = os.environ.get('REPO_VISIBILITY')
now = datetime.datetime.now()

#local
'''
repo_name = 'ravilladhaneesh/github-viewer'
repo_path = os.getcwd()
repo_branch = 'dummy'
repo_url = 'https://github.com/ravilladhaneesh/github-viewer'
'''



print(f"repo name: {repo_name}")
print('---------------------')
print(f'repo path: {repo_path}')
print('---------------------')
print(f'repo url: {repo_url}')
print('---------------------')
print(f'branch: {repo_branch}')
print('---------------------')
print(f'visibility: {repo_visibility}')
print('---------------------')
print(f'current time: {now}')
print('---------------------')


def get_files_of_non_master_branch(repo_path):
 
    excluded_dirs = {'.git', '.github', 'github-scraper'}
    #local testing
    #excluded_dirs = = {'.git', '.github', 'github-scraper', '.venv', '__pycache__'}
    USERNAME, REPO = repo_name.split('/')

    #file_extensions = ['py', 'css', 'html', 'txt', 'java']

    file_extensions = {}

    for dirpath, dirnames, filenames in os.walk(repo_path):
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs]
                
        #print(f"\nDirectory: {dirpath}")
                
        for file in filenames:
            #print(f"  File: {file}")
            if not file.startswith('.git'):
                extension = file.split('.')[-1]
                if extension in file_extensions:
                    file_extensions[extension] += 1
                else:
                    file_extensions[extension] = 1

    for extension, value in file_extensions.items():
        print(extension, value)
    return file_extensions

def get_languages_percentage(languages):
    cal_percentage = lambda x: (x / percentage_sum ) * 100
    percentage_sum = sum(languages.values())
    languages_percentage = {lang: round(cal_percentage(languages[lang]), 2) for lang in languages}
    print(languages_percentage)
    return languages_percentage


def process_repo(name, branch, url, path):

    default_branches = {'master', 'main'}
    
    if branch in default_branches:
        languages_data = git_api.get_languages(name)
    else:
        languages_data = get_files_of_non_master_branch(path)
        

    languages_percentage = get_languages_percentage(languages_data)


process_repo(repo_name, repo_branch, repo_url, repo_path)
