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


if __name__ == "__main__":
    Log = os.path.exists(
        r"C:\Users\KAUSTAV\Documents\CrT GitHub CLI\username.txt")
    if Log == False:
        username = input("Enter username of GitHub account: ")
        password = input("Enter password: ")
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
        while True:
            mainPath = os.getcwd()
            comd = input(f"{mainPath}: ")
            if comd == "help":
                print("No help available")
            elif comd == "exit":
                exit()
            else:
                print(f"bash: {comd}: no such command")
