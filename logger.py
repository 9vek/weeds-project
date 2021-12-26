import datetime


def console_log(info):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {info}")