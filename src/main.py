import os
import datetime



print('----------------------')
print('TEST GITHUB ACTIONS')
print('----------------------')

repo_name = os.environ.get('REPO_NAME')
repo_path = os.environ.get('REPO_PATH')
repo_url = os.environ.get('REPO_URL')
repo_branch = os.environ.get('BRANCH')
now = datetime.datetime.now()

#local
'''
repo_path = os.getcwd()
repo_name = 'ravilladhaneesh/workflow-test'
repo_path = "C:\\Users\\Gopinath\\OneDrive\\Documents\\Dhaneesh folder\\personal project\\workflow-test"
repo_url = 'https://github.com/ravilladhaneesh/workflow-test'
repo_path = "C:\\Users\\Gopinath\\OneDrive\\Documents\\Dhaneesh folder\\AI-ML"
'''


print(repo_name)
print('---------------------')
print(repo_path)
print('---------------------')
print(repo_url)
print('---------------------')
print(repo_branch)
print('---------------------')



excluded_dirs = {'.git', '.github', 'scraper'}
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
                
