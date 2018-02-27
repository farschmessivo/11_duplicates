import os
import sys
import hashlib


def find_duplicates(directory):
    duplicates = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = get_file_hash(file_path)
            if file_hash in duplicates:
                duplicates[file_hash].append(file_path)
            else:
                duplicates[file_hash] = [file_path]
    return duplicates


def get_file_hash(path, blocksize=4096):
    with open(path, 'rb') as filename:
        hasher = hashlib.md5()
        buffer = filename.read(blocksize)
        while len(buffer) > 0:
            buffer = filename.read(blocksize)
            hasher.update(buffer)
        return hasher.hexdigest()


def print_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if results:
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
    if sys.argv:
        root = sys.argv[1]
        print('Scanning... {}'.format(root))
        duplicates = find_duplicates(root)
        print_results(duplicates)
    else:
        sys.exit('Usage: python3 duplicates.py folder')
