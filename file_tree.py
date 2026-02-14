from file_size import get_file_size,convert_from_bytes
from os import listdir
from os.path import isdir

# currently it is not going in to directory

def crawl_directory(path,ignore_hidden=True):
    directory_list = listdir(path)
    if ignore_hidden:
        directory_list = [file for file in directory_list if file[0]!='.']    
    total_file_size_bytes = 0
    for file in directory_list:
        if isdir(path + '/' + file):
            file_directory_size = crawl_directory(path + '/' + file)
        elif not isdir(file):
            file_directory_size = get_file_size(path + '/' + file)

        total_file_size_bytes += file_directory_size
        
    return total_file_size_bytes


if __name__=='__main__':
    print(crawl_directory('dir1'))
    print(convert_from_bytes(crawl_directory('dir1/dir2'),'mb',1))

# base_case 
# if no files are directories return the running total

# given a directory
# loop through items in directory
# if it is a file, add its size to the running total

# if it is a directory, recursive call
