import logging
import os.path


class LogGen():
    @staticmethod
    def loggen():
        basepath = os.path.join(os.path.abspath(os.curdir)+'\\Logs\\automation.log')
        os.makedirs(os.path.dirname(basepath),exist_ok=True)
        logging.basicConfig(filename=basepath,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.WARN) #WARN,ERROR,FETAL,DEBUG,INFO
        return logger