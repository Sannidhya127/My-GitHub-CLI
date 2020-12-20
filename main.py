import github
from github import Github
import win32api
import win32con
import win32com
import os
import ctypes
import win32event
import win32process
import sys
from colored import fg, bg, attr


def repoLister(user):
    f = open(r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\username.txt")
    texts = f.read()
    f.close()
    allr = user.get_user().get_repos()
    for repo in user.get_repos():
        print(repo.name)


if __name__ == "__main__":
    Log = os.path.exists(
        r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\username.txt")
    if Log == False:
        global username
        global password
        username = input("Enter username of GitHub account: ")
        password = input("Enter password: ")
        global g
        global user
        g = Github(username, password)
        user = g.get_user()
        # user.login
        try:
            g = Github(username, password)
            user = g.get_user(username)
            user.login
            os.mkdir(r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI")
            UserLogged = open(
                r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\username.txt", "w")
            UserPass = open(
                r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\userpass.txt", "w")
            UserLogged.write(username)
            UserPass.write(password)
        except Exception as e:
            print(e)
    else:
        try:
            UserLogged = open(
                r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\username.txt", "r")
            UserPass = open(
                r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\userpass.txt", "r")
            name = UserLogged.read()
            password = UserPass.read()
            print(name)
            print(password)
            # g = Github(name, password)
            # user = g.get_user()
            # user.login
            while True:
                mainPath = os.getcwd()
                comd = input(f"{fg('green_1')}{mainPath}: {attr('reset')}")
                if comd == "help" or comd == "help me":
                    print("No help available")
                elif comd == "lsr":
                    repoLister(user.name)

                elif comd == "exit":
                    exit()
                else:
                    print(
                        f"{fg('red_1')}bash: '{comd}': no such command{attr('reset')}")

        except Exception as e:
            print(e)
