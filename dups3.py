import sys, os, os.path, hashlib

dupe_directory = sys.argv[1]
search_directory = sys.argv[2]

# dupe dictionary: absolute_path -> file_size
# search dictionary: file_size -> list of absolute_path

dupe_dictionary, search_dictionary, hash_dictionary = dict(), dict(), dict()

#
# def get_file_size(absolute_path):
#     return os.path.getsize(absolute_path)


def get_hash(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def match_on_hash(dupe_file):
    for search_file in search_dictionary[file_size]:
        if search_file not in hash_dictionary:
            hash_dictionary[search_file] = get_hash(search_file)
        if dupe_file not in hash_dictionary:
            hash_dictionary[dupe_file] = get_hash(dupe_file)
        search_hash = hash_dictionary[search_file]
        dupe_hash = hash_dictionary[dupe_file]
        if search_hash != dupe_hash:
            return dupe_file


for dirpath, dirnames, filenames in os.walk(dupe_directory):
    for filename in filenames:
        absolute_path = os.path.join(dirpath, filename)
        dupe_dictionary[absolute_path] = os.path.getsize(absolute_path)

for dirpath, dirnames, filenames in os.walk(search_directory):
    for filename in filenames:
        absolute_path = os.path.join(dirpath, filename)
        file_size = os.path.getsize(absolute_path)
        if file_size not in search_dictionary:
            search_dictionary[file_size] = []
        search_dictionary[file_size].append(absolute_path)

for dupe_file in dupe_dictionary:
    file_size = dupe_dictionary[dupe_file]
    if file_size in search_dictionary:
        match_on_hash(dupe_file)

#
# if __name__ == '__main__':
#     pass
