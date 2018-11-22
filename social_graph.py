import matplotlib.pyplot as plt
import numpy as np
from github import Github   # PyGithub: https://github.com/PyGithub/PyGithub

def getLanguageDetails(user):
    languageDict = dict()

    for repo in user.get_repos():
        language = repo.language
        if language in languageDict:
            languageDict[language] = languageDict[language] + 1
        else:
            languageDict[language] = 1

    return languageDict

def getAvgLanguageDetails(dictList):
    

def pieChart(values, labels, title):
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(title)
    plt.show()
# print("Hi, Welcome to Yet Another GitHub Analytics Program!\n\nHow would you like to sign in?\n\n1 = Username & Password\n2 = Token\n")

# Login prompts
# while (True):
#     choice = int(input("Enter your choice: "))
#     if (choice == 1):
#         g = Github(input("Username: "), input("Password: "))
#         break
#     elif (choice == 2):
#         print("You can get the token from the developer settings in GitHub")
#         g = Github(str(input("Token: ")))
#         break
#     else:
#         print("Invalid, choose 1 or 2")


g = Github("dominickcleary@gmail.com", "q2,)=|w?4'Qq&x")

# Login
user = g.get_user()

# dict = getLanguageDetails(user)
# pieChart(dict.values(), dict, user.name + "'s language stats")
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