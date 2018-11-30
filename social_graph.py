import matplotlib.pyplot as plt
import numpy as np
from github import Github  # PyGithub: https://github.com/PyGithub/PyGithub


# Returns a dictionary containing the language used and amount of repos that use them
def get_language_details(user):
    language_dict = dict()

    for repo in user.get_repos():
        language = str(repo.language)
        if language in language_dict:
            language_dict[language] = language_dict[language] + 1
        else:
            language_dict[language] = 1

    return language_dict


# Converts the dictionary list into one dictionary
def get_avg_language_details(dict_list):
    new_dict = dict()

    for dicts in dict_list:
        for key, value in dicts.items():
            if key not in new_dict:
                new_dict[key] = value
            else:
                new_dict[key] = new_dict[key] + value

    return new_dict


# Creates one pie chart
def pie_chart(values, labels, title, window_name):
    plt.figure(num=window_name)
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title)

    plt.show()


# Creates two pie charts side by side
def pie_chart_two(values1, labels1, values2, labels2, title1, title2, window_name):
    plt.figure(num=window_name)
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
def bar_chart(x, y, x_label, y_label, title, window_name):
    plt.figure(num=window_name)
    y_pos = np.arange(len(y))

    plt.bar(y_pos, list(x), align='center')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.yticks(y_pos, y)
    plt.title(title)

    plt.show()


# Creates a horizontal bar chart
def bar_chart_h(x, y, x_label, y_label, title, window_name):
    plt.figure(num=window_name)
    y_pos = np.arange(len(y))

    plt.barh(y_pos, list(x), align='center')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.yticks(y_pos, y)
    plt.title(title)

    plt.show()


# Compares the logged in users language stats to those they follow
def compare_language_use(user):
    dict_list = []

    for follower in user.get_following():
        dict_list.append(get_language_details(follower))

    avg_dict = get_avg_language_details(dict_list)
    user_dict = get_language_details(user)
    pie_chart_two(user_dict.values(), user_dict, avg_dict.values(), avg_dict, user.name + "'s Language Use",
                  "Followers Average Language Use", "Comparison of languages used")


# Compares the amount of commits between all the users repos
def compare_commits_per_repo(user):
    repo_info = dict()
    for repo in user.get_repos():
        count = 0
        for commit in repo.get_commits():
            count += 1
        repo_info[repo.name] = count
    bar_chart_h(repo_info.values(), repo_info, "Commits", "Repos", "Amount of Commits per Repo",
                "Amount of Commits per Repo")


def compare_commit_days(user):
    day_list = [0] * 7
    for repo in user.get_repos():
        for commit in repo.get_commits():
            weekday = commit.commit.author.date.weekday()
            day_list[weekday] = day_list[weekday] + 1
    pie_chart(day_list, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
              "Distribution of Days that " + user.name + " Commits on", "Comparison of Commit Days")


print(
    "Hi, Welcome to Yet Another GitHub Analytics Program!\n\nHow would you like to sign in?\n\n1 = Username & "
    "Password\n2 = Token\n")

# Login prompts
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        g = Github(input("Username: "), input("Password: "))
        break
    elif choice == 2:
        print("You can get the token from the developer settings in GitHub")
        g = Github(str(input("Token: ")))
        break
    else:
        print("Invalid, choose 1 or 2")

# Login
user = g.get_user()
# Run through analytics windows
compare_language_use(user)
compare_commits_per_repo(user)
compare_commit_days(user)
