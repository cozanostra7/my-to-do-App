FILEPATH='activities.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file_local:
        content = file_local.readlines()

        return content

def write_todos(content,filepath=FILEPATH):
    with open(filepath,'w') as file_local:
        file_local.writelines(content)