from github import Github   # PyGithub: https://github.com/PyGithub/PyGithub

# access token
g = Github("e5cfaa1eb882bd25a1bc71ba2a4214e923569bea")
user = g.get_user()

print("Details of " + user.name + "'s repositories\n")

for repo in user.get_repos():
    print("Name: " + repo.name)
    print("URL: " + repo.html_url)
    print("Language: " + str(repo.language))
    print("Stars: " + str(repo.stargazers_count))
    print("Private: " + str(repo.private) + "\n")

print("\n\n" + user.name + " has " + str(user.followers) + " followers\n")

for follower in user.get_followers():
    print("Name: " + follower.name)
    print("URL: " + follower.html_url)
    print("Public Repos: " + str(follower.public_repos) + "\n")

print("\n\nAnd follows " + str(user.following) + " users\n")

for followe in user.get_following():
    print("Name: " + followe.name)
    print("URL: " + followe.url)
    print("Public Repos: " + str(followe.public_repos) + "\n")