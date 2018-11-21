import matplotlib.pyplot as plt
import numpy as np
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

# Compares the logged in users language stats to those they follow
def compareLanguageUse(user):
    dictList = []
    
    for follower in user.get_following():
        dictList.append(getLanguageDetails(follower))

    avgDict = getAvgLanguageDetails(dictList)
    userDict = getLanguageDetails(user)
    pieChart(userDict.values(), userDict, avgDict.values(), avgDict, user.name + "'s Language Use", "Followers Average Language Use")
    
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
compareLanguageUse(user)
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