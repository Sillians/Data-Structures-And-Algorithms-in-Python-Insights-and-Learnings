import os

def disk_usage(path: os.path):
    """Return the number of bytes used by a file/folder and any descendants"""

    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total

# Time Complexity: O(n)
path = "path-to-file"
print(disk_usage(path))