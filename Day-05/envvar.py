import os

print(os.getenv("GITHUB_SERVER_URL"))
print(os.getenv("VSCODE_GIT_IPC_HANDLE"))
print(os.getenv("dummy"))
print(os.getenv("dfddfdf"))

os.environ.pop("dummy", None)

print(os.getenv("dummy"))