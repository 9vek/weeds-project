import os
import os.path as osp
from pathlib import Path

def list_files(path, ignore_files):
  path = Path(path)
  files = list(path.glob('*'))

  for file in files:

    if file.is_dir():
      files.remove(file)

    for ifile in ignore_files:
      if file.match(ifile):
        files.remove(file)

  return files


def list_files_r(path: str, ignore_files):
  path.replace('/', osp.sep)
  files = next(osp.walk(path), (None, None, []))[2]

  for file in ignore_files:
    if file in files:
      files.remove(file)

  return files
