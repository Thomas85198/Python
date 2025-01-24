import os
import sys

filepath = "whatever\\some==directory\\path.jpg"
print(os.path.basename(filepath))  # path.jpg
print(os.path.split(filepath))  # ('whatever\\some==directory', 'path.jpg')
# C:\Users\user\whatever\some==directory\path.jpg
print(os.path.abspath(filepath))

print(os.name)  # nt
print(sys.platform)  # win32
print("測試中文")
