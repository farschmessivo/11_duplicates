import os
import sys
import hashlib


def find_duplicates(directory):
    # Dups in format {hash:[names]}
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        print('Scanning %s...' % root)
        for filename in files:
            # Get the path to the file
            file_path = os.path.join(root, filename)
            # Calculate hash
            file_hash = hashfile(file_path)
            # Add or append the file path
            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]
    return duplicates


def join_dictionaries(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def hashfile(path, blocksize=4096):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.close()
    return hasher.hexdigest()


def print_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('The following files are identical.')
        print('The name could differ, but the content is identical')
        print('___________________')
        print('Duplicates Found:')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')

    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    if len(sys.argv) > 0:
        duplicates = {}
        root = sys.argv[1:2]
        for directory in root:
            # Iterate the folders given
            if os.path.exists(directory):
                # Find the duplicated files and append them to the dups
                join_dictionaries(duplicates, find_duplicates(directory))
            else:
                print('%s is not a valid path, please verify' % directory)
                sys.exit()
        print_results(duplicates)
    else:
        print('Usage: python3 duplicates.py folder')
