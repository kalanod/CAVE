import os.path
def get_files_sizes():
    a = os.listdir("data")
    for i in a:
        print("             ('data/"+i+"', 'data'),")


get_files_sizes()