import os
def getdir_path(sub_dir=""):
    project_path = os.path.dirname(os.path.dirname(__file__))
    if sub_dir:
        return os.path.join(project_path, sub_dir)
    return project_path