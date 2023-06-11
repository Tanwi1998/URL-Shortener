import requests
import json
import time
from github import Github, GithubException


token = "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"
profile = Github(token)
accessUser = profile.get_user()
get_all_repo = accessUser.get_repos()


# ---------- TO GET INFO ABOUT REPOSITORY ----------
def info_repo(token):
    repo = input("\r Name the repository to extract the details : ")
    get_repo = accessUser.get_repo(repo)
    print(get_repo.name)
    print(get_repo.description)
    print(get_repo.contributors_url)
    print(get_repo.language)
    contributors = get_repo.get_contributors()
    for cont in contributors:
        print("\r", cont.login)

# ---------- TO CREATE AN ISSUE IN REPOSITORY ----------


def creating_issue(token):
    issue_repo = input("\r Name the repository to create an issue : ")
    repo = accessUser.get_repo(issue_repo)
    title = input("\r Give a title : ")
    body = input("\r Give a description : ")
    repo.create_issue(title=title, body=body)

# ---------- TO CREATE A NEW REPOSITORY ----------


def create_new_repo(token):
    newRepo = input("\r Name the new repository : ")
    description = input("\r Give a description : ")
    repos = accessUser.create_repo(
        name=newRepo, description=description, private=True)

# ---------- TO CREATE A NEW COMMIT, PULL REQUEST & MERGE ----------







# ---------- TO CREATE A NEW FILE IN AN EXISTING REPOSITORY ----------
def create_repo_file(token):
    allRepo = []
    for repo in get_all_repo:
        allRepo.append(repo.name)
    print(allRepo)
    select_repo = input("\r Choose a repository from above : ")
    if select_repo in allRepo:
        selected_repo = accessUser.get_repo(select_repo)
        # path = input("\r Write the path to create a file within : ")
        newFile = input("\r Name the new file : ")
        content = input("\r Write the content for the file : ")
        try:
            file = selected_repo.create_file(
                newFile, "New file", content)
        except Exception as e:
            print(f"\r Error is {e}")
    else:
        print("\r Invalid repository")


# ---------- TO DELETE A REPOSITORY ----------
def delete_repo(token):
    repo = input("\r Enter name of the repository to delete : ")
    get_repo = accessUser.get_repo(repo)
    get_repo.delete()


# ---------- TO DELETE A FILE IN AN EXISTING REPOSITORY ----------
def delete_repo_file(token):
    search_ele = input(f"\r Choose a repository : ")
    for idx, repo in enumerate(get_all_repo):
        if repo.name == search_ele:
            file_path = input("\r Enter the file path for deletion : ")
            file = repo.get_contents(file_path)
            repo.delete_file(file_path, 'Deleting file', file.sha)


# ---------- TO SEARCH A REPOSITORY ----------
def search_repo(token):
    allRepo = []
    for repo in get_all_repo:
        allRepo.append(repo.name)
    search_ele = input("\r Enter the repository to search : ")
    if search_ele in allRepo:
        print("\r Found")
    else:
        print("\r Not found")


def choose_option():
    option = input(
        "\r 1. Create A New Repository \n 2. Create A New File In An Existing Repository \n 3. Delete A File In an Existing Repository \n 4. Search An Existing Repository \n 5. Delete A Repository \n 6. Get Details Of A Repository \n 7. Create An Issue In A Repository \n 8. Exit \n Choose either of above options : ")
    if option == "1":
        create_new_repo(token)
    elif option == "2":
        create_repo_file(token)
    elif option == "3":
        delete_repo_file(token)
    elif option == "4":
        search_repo(token)
    elif option == "5":
        delete_repo(token)
    elif option == "6":
        info_repo(token)
    elif option == "7":
        creating_issue(token)
    elif option == "8":
        exit()
    else:
        print("\r Invalid option")

# if choose_option() == "1":
#     create_new_repo(token)
# elif choose_option() == "2":
#     create_repo_file(token)
# elif choose_option() == "3":
#     delete_repo_file(token)
# elif choose_option() == "4":
#     search_repo(token)
# elif choose_option() == "5":
#     delete_repo(token)
# elif choose_option()=="6":
#     info_repo(token)
# elif choose_option()=="7":
#     creating_issue(token)
# elif choose_option()=="8":
#     exit()


create_repo_file(token)
