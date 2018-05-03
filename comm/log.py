import logging
import configparser
from logging import handlers


class Loger(logging.Logger):
    def __init__(self, filename=None):
        super(Loger, self).__init__(self)
        # 日志文件名
        cf = configparser.ConfigParser()
        cf.read(r'F:\pythonproject\oa_test\config.ini')
        filename = cf.get('REPORT', 'log_path')
        self.filename = filename
        # 创建一个handler，用于写入日志文件
        fh = logging.handlers.RotatingFileHandler(self.filename, 'a')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter_fh = logging.Formatter(
            '[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s] - %(message)s')
        formatter_ch = logging.Formatter('[%(asctime)s] - %(message)s')
        fh.setFormatter(formatter_fh)
        ch.setFormatter(formatter_ch)

        # 给logger添加handler
        self.addHandler(fh)
        #该日志输出到控制台
        self.addHandler(ch)