import os
import os.path as  osp
from pathlib import Path
import logger as l


def select_folder() -> Path:
  path = ''
  while True:
    print('输入文件夹路径：', end='')
    path = Path(input())
    if path.is_dir:
      l.console_log('路经选择成功。')
      return path
    else:
      l.console_log('无效的文件夹，请重新输入。')


def select_symbol(selections):
  while True:
      print('请选择：', end='')
      symbol = input().lower()
      if symbol.split(' ')[0] in selections:
        return symbol
      else:
        l.console_log('无效的输入，再试一次。')


def vali_path(path):
  the_path = Path(path)
  counter = 1
  while True:
    if not the_path.exists():
      return the_path
    else:
      the_path = Path(path + f'({counter})')
      counter += 1
