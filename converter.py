import os
import convertapi

# import aspose.cad as cad

folderPath = './'
folder = os.listdir(folderPath)
convertapi.api_credentials = 'bSFyPLCwAlGwNNA3gHTUjocFcq1w1wbL'


def convert(file_path, save_path, format):
    result = convertapi.convert('png', {
        'File': file_path,
        'ImageAntialiasing': '0'
    }, from_format=format)
    result.file.save(save_path)


# def convert(file_path, save_path, format):
#     image = cad.Image.load(file_path)
#     rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
#     rasterizationOptions.layouts = ["Model"]
#     options = cad.imageoptions.PngOptions()
#     options.vector_rasterization_options = rasterizationOptions
#     image.save(save_path, options)


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
        elif ext in ['dwg', 'dxf', 'DWG', 'DXF']:
            if not os.path.isfile(path.replace(f'.{ext}', '.png')):
                convert(path, path.replace(f'.{ext}', '.png'), ext)


print_files_in_dir('./', '')

# convert('./[CannonKeys] Brutal60/brutal60_standard.dxf', './[CannonKeys] Brutal60/brutal60_standard.png', 'dxf')
