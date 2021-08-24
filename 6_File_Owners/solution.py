
def group_by_owners(files):
    owner_files = {}
    for file, owner in files.items():
        owner_files.setdefault(owner, []).append(file)

    return owner_files


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))

# {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
