import matplotlib.pyplot as plt
import numpy as np
from random import randint
from github import Github   # PyGithub: https://github.com/PyGithub/PyGithub

# Returns a dictionary containing the language used and amount of repos that use them
def getLanguageDetails(user):
    languageDict = dict()

    for repo in user.get_repos():
        language = str(repo.language)
        if language in languageDict:
            languageDict[language] = languageDict[language] + 1
        else:
            languageDict[language] = 1

    return languageDict

# Converts the dictlist into one dict
def getAvgLanguageDetails(dictList):
    newDict = dict()

    for dicts in dictList:
        for key, value in dicts.items():
            if key not in newDict:
                newDict[key] = value
            else:
                newDict[key] = newDict[key] + value

    return newDict
    
# Creates two pie charts side by side
def pieChart(values1, labels1, values2, labels2, title1, title2):
    
    plt.subplot(1, 2, 1)
    plt.pie(values1, labels=labels1, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title1)

    plt.subplot(1, 2, 2)
    plt.pie(values2, labels=labels2, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title2)

    plt.show()

# Creates a bar chart
def barChartH(x, y, xlabel, ylabel, title):
    y_pos = np.arange(len(y))

    plt.barh(y_pos, list(x), align='center')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yticks(y_pos, y)
    plt.title(title)
    
    plt.show()

# Compares the logged in users language stats to those they follow
def compareLanguageUse(user):
    dictList = []
    
    for follower in user.get_following():
        dictList.append(getLanguageDetails(follower))

    avgDict = getAvgLanguageDetails(dictList)
    userDict = getLanguageDetails(user)
    pieChart(userDict.values(), userDict, avgDict.values(), avgDict, user.name + "'s Language Use", "Followers Average Language Use")

# Compares the amount of commits between all the users repos
def compareCommitsPerRepo(user):
    repoInfo = dict()
    for repo in user.get_repos():
        count = 0
        for commit in repo.get_commits():
            count += 1
        repoInfo[repo.name] = count
    barChartH(repoInfo.values(), repoInfo, "Commits", "Repos", "Amount of Commits per Repo")


    
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


g = Github("860f00f494ad2a882e4a9ed1a7f55f9598bd9add")

# Login
user = g.get_user()
# compareLanguageUse(user)
compareCommitsPerRepo(user)

