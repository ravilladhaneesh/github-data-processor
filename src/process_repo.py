import os

file_extensions = {
    'py': 'python',
    'java': 'java',
    'c': 'C', 
    'cpp': 'c++',
    'js': 'javascript',
    'html': 'HTML',
    'css': 'CSS',
    'tf': 'HCL',
    'txt': 'text',
    'json': 'JSON',
    'md': 'markdown'
}


"""
Function to find all the different files in the directory
"""
def get_files_of_non_default_branch(repo_name, repo_path):
     
    excluded_dirs = { 'github-data-processor', '__pycache__'}
    #local testing
    #excluded_dirs = = {'.git', '.github', 'github-data-processor', '.venv', '__pycache__'}
    USERNAME, REPO = repo_name.split('/')

    #file_extensions = ['py', 'css', 'html', 'txt', 'java']

    file_extensions = {}

    for dirpath, dirnames, filenames in os.walk(repo_path):
        
        # print('\nDirnames', dirnames)
        # print(f"\nDirectory: {dirpath}")
        # print("\nfilesNames:", filenames)
        dirnames[:] = [d for d in dirnames if d not in excluded_dirs and not d.startswith(".")]
                
        for file in filenames:
            #print(f"  File: {file}")
            if not file.startswith('.git'):
                extension = file.split('.')[-1]
                if extension in file_extensions:
                    file_extensions[extension] += 1
                else:
                    file_extensions[extension] = 1
        # print("\n-------------------------\n")

    for extension, value in file_extensions.items():
        print(extension, value)
    return file_extensions

"""
Calculate the percentage of each file in the repo based on count
"""
def get_languages_percentage(languages):
    cal_percentage = lambda x: (x / percentage_sum ) * 100
    percentage_sum = sum(languages.values())
    languages_percentage = {lang: round(cal_percentage(languages[lang]), 2) for lang in languages}
    #print(languages_percentage)
    return languages_percentage


"""
The function processes the languages dictionary with file extensions shortform as keys and
return keys with know file extension name

Ex: .py as python, .tf as HCL
"""
def get_languages(languages):
    lang = {}
    for key, value in languages.items():
        if key in file_extensions.keys():
            lang[file_extensions[key]] = value
        else:
            lang[key] = value
    
    return lang
