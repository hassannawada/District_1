import os
from datetime import datetime, timedelta

def scan_folder(folder):
    """Returns list of file details."""
    files = []
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            info = os.stat(path)
            files.append({
                "name": name,
                "size": info.st_size,
                "type": os.path.splitext(name)[1],
                "modified": datetime.fromtimestamp(info.st_mtime),
            })
    return files

def days_old(modified):
    """How many days since the file was changed."""
    return (datetime.now() - modified).days

def fine(modified):
    """Rs 5 fine for every day after 30 days."""
    extra = days_old(modified) - 30
    if extra > 0:
        return extra * 5
    return 0

if __name__ == "__main__":
    print(scan_folder("."))
