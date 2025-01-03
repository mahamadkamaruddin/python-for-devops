import os


#function to list the files under the folder given
def ListFiles(FolderList):
    
    for folder in FolderList:
        print("\nlisting the files for the folder {}:\n".format(folder))
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            print("folder {} not found".format(folder))
            continue
        except PermissionError:
            # print("User has no acces to dir")
            break
        for file in files:
            print(file)

#main funtction to collect the folder in a list/array
def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split()

    ListFiles(folder_paths)
    


#main invoke
if __name__ == "__main__":
    main()
