import os

for key, val in os.environ.items():
    if key in [
        "BUILD_REPOSITORY_URI",
        "BUILD_DEFINITIONVERSION",
        "BUILD_SOURCEVERSIONAUTHOR",
        "BUILD_REPOSITORY_NAME",
        "TASK_DISPLAYNAME",
        "RESOURCES_TRIGGERINGCATEGORY",
        "SYSTEM_PULLREQUEST_ISFORK",
        "BUILD_SOURCEVERSION",
        "BUILD_REASON",
        "BUILD_SOURCEBRANCH",
        "BUILD_REQUESTEDFOR",
    ]:
        print(key, "     ", val)
    elif "PULLREQUEST" in key or "PULL_REQUEST" in key:
        print(key, "    ", val)