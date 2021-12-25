from os import listdir, walk
from os.path import isfile, join, sep

ignore_files = [
  'desktop.ini'
]

def list_files(path: str):
  path.replace('/', sep)
  files = [
    f for f in listdir(path) if isfile(join(path, f))
  ]

  for file in ignore_files:
    if file in files:
      files.remove(file)

  return files


def list_files_r(path: str):
  path.replace('/', sep)
  files = next(walk(path), (None, None, []))[2]

  for file in ignore_files:
    
    if file in files:
      files.remove(file)

  return files
