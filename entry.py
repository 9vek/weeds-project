import os
from os.path import sep
import logger
import manage as m


if __name__ == '__main__':

  # 初始化
  if (logger.has_log('weeds')):
    logger.console_log('欢迎回到 weeds !')

  else:
    logger.console_log('发现您是首次运行 weeds ，请完成设置。')

    # 设置存储路径
    logger.console_log('输入您希望创建 weeds 文件夹的位置：')
    store_path = m.select_folder()

    # 设置路径类型
    logger.console_log('您希望将该路径保存为绝对（a）还是相对（r）？')
    path_type = m.select_symbol(['a', 'r'])
    if path_type == 'a':
      store_path = os.path.abspath(store_path)
    elif path_type == 'r':
      store_path = os.path.relpath(store_path)

    # 初始化 weeds 文件夹
    logger.console_log('正在初始化 weeds 文件夹。')
    m.weeds_init(store_path)

    # 生成配置文件
    logger.console_log('正在生成配置文件。')
    config = {
      'store_path': store_path + sep + 'weeds' + sep, 
      'path_type': path_type,
      'weeds': [
        
      ]
    }
    logger.write_log('weeds', config)
    
    logger.console_log('欢迎回到 weeds 程序！')

  # 进入 weeds 程序
  m.weeds_loop()



