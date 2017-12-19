import os
import sys
import hashlib


def find_duplicates(directory):
    # Dups in format {hash:[names]}
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        print('Scanning %s...' % root)
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = hashfile(file_path)
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
        root = sys.argv[1]
        if os.path.exists(root):
            join_dictionaries(duplicates, find_duplicates(root))
        else:
            print('%s is not a valid path, please verify' % root)
            sys.exit()
        print_results(duplicates)
    else:
        print('Usage: python3 dups3.py folder')
