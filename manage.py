import os.path
from os.path import sep
import logger

def select_folder():
  path = ''
  while True:
    print('输入文件夹路径：', end='')
    path = input().replace('/', os.path.sep)
    if os.path.isdir(path):
      logger.console_log('路经选择成功。')
      return path
    else:
      logger.console_log('无效的文件夹，请重新输入。')


def select_symbol(selections):
  while True:
      print('请选择：', end='')
      symbol = input().lower()
      if symbol in selections:
        return symbol
      else:
        logger.console_log('无效的输入，再试一次。')


def weeds_init(path):
    os.mkdir(f'{path + sep}weeds')
    os.mkdir(f'{path + sep}weeds{sep}doc')
    os.mkdir(f'{path + sep}weeds{sep}zip')
    os.mkdir(f'{path + sep}weeds{sep}exe')
    os.mkdir(f'{path + sep}weeds{sep}img')
    os.mkdir(f'{path + sep}weeds{sep}oth')


def addw(config):
  logger.console_log('输入您希望 weeds 开展管理的位置：')
  new_weed = select_folder()
  new_weed = os.path.abspath(new_weed)
  config['weeds'].append({
    'path': new_weed + sep
  })


def generate_menu(props):

  menu = '''

  '''

  for k, v in props.items(): menu += f'''{k}: {v}
  '''
  return menu


def weeds_loop():

  config = logger.read_log('weeds')

  cmds = {
    'weed': '除草！',
    'addw': '添加一个需要整理的位置',
    'help': '显示命令菜单',
    'pcfg': '显示配置信息',
    'quit': '退出 weeds 程序'
  }
  
  cmd = ''
  logger.console_log(generate_menu(cmds))
  while True:
    cmd = select_symbol(cmds.keys())
    if cmd == 'quit':
      logger.override_log('weeds', config)
      logger.console_log('感谢您的使用，再见！')
      break
    elif cmd == 'help':
      logger.console_log(generate_menu(cmds))
    elif cmd == 'pcfg':
      logger.console_log(config)
    elif cmd == 'addw':
      addw(config)