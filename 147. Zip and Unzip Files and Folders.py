import zipfile

zipped_file = zipfile.ZipFile('research.zip', 'w')
zipped_file.write('research.txt', compress_type=zipfile.ZIP_DEFLATED)
zipped_file.close()
