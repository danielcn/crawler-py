import os

# Each webisite you crawl is a separete project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Create project" + directory)
        os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, 'cd .')

# Create a new file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

create_data_files('thenewboston', 'http://thenewboston.com/')
