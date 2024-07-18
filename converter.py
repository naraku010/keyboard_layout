import os
import convertapi

folderPath = './'
folder = os.listdir(folderPath)
convertapi.api_secret = 'V4cjRpwQxmRcml8K'

def convert(file_path, save_path, format):
    result = convertapi.convert('png', {
        'File': file_path
    }, from_format=format)
    result.file.save(save_path)

def print_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        print('path:', prefix, '  path:', path)
        fname, ext = os.path.splitext(file)
        ext = ext.replace('.', '')
        print(f'FILE: {fname}.{ext}')
        if os.path.isdir(path):
            print_files_in_dir(path, prefix + "    ")
        elif ext in ['dwg', 'dxf']:
            convert(path, path.replace(f'.{ext}', '.png'), ext)

print_files_in_dir('./Matrix 3.3', '')

# convert('./Brutal60/brutal60_standard.dxf', './Brutal60/brutal60_standard.png', 'dxf')
