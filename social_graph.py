import matplotlib.pyplot as plt
import numpy as np
from github import Github   # PyGithub: https://github.com/PyGithub/PyGithub

print("Hi, Welcome to Yet Another GitHub Analytics Program!\n\nHow would you like to sign in?\n\n1 = Username & Password\n2 = Token\n")

while (True):
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        g = Github(input("Username: "), input("Password: "))
        break
    elif (choice == 2):
        print("You can get the token from the developer settings in GitHub")
        g = Github(str(input("Token: ")))
        break
    else:
        print("Invalid, choose 1 or 2")
        
# Login
user = g.get_user()

print("Details of " + user.name + "'s repositories\n")

for repo in user.get_repos():
    print("Name: " + repo.name)
    print("URL: " + repo.html_url)
    print("Language: " + str(repo.language))
    print("Stars: " + str(repo.stargazers_count))
    print("Private: " + str(repo.private) + "\n")

# print("\n\n" + user.name + " has " + str(user.followers) + " followers\n")

# for follower in user.get_followers():
#     print("Name: " + follower.name)
#     print("URL: " + follower.html_url)
#     print("Public Repos: " + str(follower.public_repos) + "\n")

# print("\n\nAnd follows " + str(user.following) + " users\n")

# for followe in user.get_following():
#     print("Name: " + followe.name)
#     print("URL: " + followe.html_url)
#     print("Public Repos: " + str(followe.public_repos) + "\n")