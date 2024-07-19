import os

folderPath = './'
folder = os.listdir(folderPath)


def convert(path):
    str = ''
    files = os.listdir(path)
    for file in files:
        fname, ext = os.path.splitext(file)
        print(f'{fname} {ext}')
        if ext == '.png':
            str += '<br/>'
            str += f'{fname}'
            str += '<br/>'
            str += f'![image](./{fname}{ext})'
    with open(f'{path}\README.md', 'w', encoding='utf-8') as f:
        f.write(str)



def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        if os.path.isdir(path):
            convert(path)


print_files_in_dir('./', '')

convert('./[Ai03] Andromeda')
