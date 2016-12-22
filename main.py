import os

# Each webisite you crawl is a separete project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Create project" + directory)
        os.makedirs(directory)

create_project_dir('thenewboston')
