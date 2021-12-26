import os.path as osp
from pathlib import Path
from datetime import datetime
import re
import json
import utils as u
import configer as c
import filer as f


def read_pairs(config):
  file_path = Path(config['store_path'] / '/pairs.json')
  if file_path.exists():
    with open(file_path, 'r') as json_file:
      pairs = json.load(json_file)
      return pairs
  else:
      return None


def write_pairs(pairs, config):
  file_path = Path(config['store_path'] / '/pairs.json')
  json_str = json.dumps(pairs)
  with open(file_path, 'w+') as json_file:
    json_file.write(json_str)


def addw(config, args):
  result = '\n\n'
  for path in args:
    path = Path(path)
    if path.is_dir():
      new_weed = path.absolute().as_posix()
      if c.has_w(config, new_weed):
        result += f'  路径 {new_weed} 已经存在。\n'
      else:
        config['weeds'].append({
          'path': new_weed
        })
        result += f'  添加路径 {new_weed} 成功。\n'
    else: 
      result += f'  无效的路径 {path}。\n'
  
  return result


def chkw(config, args, inner=False):
  sorted_files = {}
  result = '\n\n'
  for path in args:
    path = Path(path)
    if not path.is_dir():
      result += f'  无效的位置：{path.absolute().as_posix()}。\n'
      continue
    path = path.absolute().as_posix()
    result += f'  位置：{path}：\n'
    files = f.list_files(path, config['ignore_files'])
    for file in files:
      filename = file.split(osp.sep)[-1]
      sub_type = filename.split('.')[-1]
      sorted_files[file] = {
        'type': 'oth',
        'sub_type': sub_type,
        'filename': filename
      }

    for key in config.keys():
      if '_folder' in key:
        cur_type = key.split('_')[0]
        regs = config[key]
        reg = '(' + ')|('.join(regs) + ')'
        for file in sorted_files.values():
          if re.match(reg, file['filename']):
            file['type'] = cur_type

    for file in sorted_files.values():
      result += f'    [{file["type"]} : {file["sub_type"]}] {file["filename"]}\n'

  return sorted_files if inner else result


def weed(config, args):
  pairs = read_pairs(config)

  sorted_files = chkw(config, args, inner=True)
  for k,v in sorted_files.items():

    origin_folder = Path(k).parent.absolute().as_posix()
    if not origin_folder in pairs:
      pairs[origin_folder] = []

    origin_path = k
    new_path = Path(config['store_path'] / v['type'] / v['filename'])
    new_path = u.vali_path(new_path)
    pairs[origin_folder].append({
      'from': origin_path,
      'now': new_path,
      'since': datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    })

  # write_pairs(pairs, config)
  return pairs



def whelp(config, args):
  return generate_menu()


def pcfg(config, args):
  return config


def wquit(config, args):
  c.save_config(config)
  return '感谢您的使用，再见！'


cmds = {
  'addw': {
    'desc': '添加一个需要整理的位置',
    'func': addw
  },
  'chkw': {
    'desc': '检查一个位置的文件',
    'func': chkw
  },
  'weed': {
    'desc': '开始除草',
    'func': weed
  },
  'help': {
    'desc': '显示命令菜单',
    'func': whelp
  },
  'pcfg': {
    'desc': '显示配置信息',
    'func': pcfg
  },
  'quit': {
    'desc': '退出 weeds 程序',
    'func': wquit
  }
}


def generate_menu():
  menu = '\n\n'
  for k, v in cmds.items(): menu += f'  {k}: {v["desc"]}\n'
  return menu


def get_cmd():
  cmd = u.select_symbol(cmds.keys())
  return cmd.split(' ')


def execute(cmd, config):
  args = cmd[1:]
  message = cmds[cmd[0]]['func'](config, args)
  return message