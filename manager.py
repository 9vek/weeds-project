import utils as u
import configer as c
import handler as h
import logger as l


def weeds_init():
  if c.has_config():
    pass

  else:
    l.console_log('发现您是首次运行 weeds ，请完成设置。')

    # 设置存储路径
    l.console_log('输入您希望创建 weeds 文件夹的位置：')
    store_path = u.select_folder()

    # 设置路径类型
    l.console_log('您希望将该路径保存为绝对（a）还是相对（r）？')
    path_type = u.select_symbol(['a', 'r'])
    if path_type == 'a':
      store_path = store_path.absolute()
    elif path_type == 'r':
      store_path = store_path.relative_to('./')

    # 生成配置文件
    l.console_log('正在生成配置文件。')
    config = c.generate_config(store_path, path_type)
    c.save_config(config)

    # 初始化 weeds 文件夹
    l.console_log('正在初始化 weeds 文件夹。')
    store_path.joinpath('weeds/').mkdir()
    h.write_pairs({}, config)
    store_path.joinpath('weeds/oth/').mkdir()
    for key in config.keys():
      if '_folder' in key:
        folder = key.split('_')[0]
        store_path.joinpath(f'weeds/oth/{folder}/').mkdir()


def weeds_loop():

  l.console_log('欢迎回到 weeds 程序！')

  config = c.load_config()
  menu = h.generate_menu()
  l.console_log(menu)

  while True:
    cmd = h.get_cmd()
    message = h.execute(cmd, config)
    l.console_log(message)

    if cmd[0] == 'quit':
      break