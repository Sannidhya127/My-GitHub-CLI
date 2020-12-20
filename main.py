import github
from github import Github
import win32api
import win32con
import os

if __name__ == "__main__":
    username = input("Enter username of GitHub account: ")
    password = input("Enter password: ")
    try:
		g = Github(username, password)
		user = g.get_user(username)
		user.login
		UserLogged = open("username", "w")
		UserLogged = open("userpass", "w")
		win32api.SetFileAttributes(
			"username", win32con.FILE_ATTRIBUTE_HIDDEN)
		win32api.SetFileAttributes(
			"userpass", win32con.FILE_ATTRIBUTE_HIDDEN)
	except Exception:
		print("Error loggin in. Try again later")
    # for repo in user.get_repos():
    #     print(repo.name)
