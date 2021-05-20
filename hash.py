import hashlib


path1 = 'vali.npz'
path2 = 'part_result.npz'

def getHash(f):
    line = f.readline()
    hash = hashlib.md5()
    while (line):
        hash.update(line)
        line = f.readline()
    return hash.hexdigest()


def IsHashEqual(f1, f2):
    str1 = getHash(f1)
    str2 = getHash(f2)
    return str1 == str2


def GetFile(path1, path2):
     with open(path1, "rb") as f1:
        with  open(path2, "rb") as f2:
                print(IsHashEqual(f1, f2))


if __name__ == '__main__':
    GetFile(path1, path2)
