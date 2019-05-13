import logging
import os

class Log(object):
    initialised = False
    logger = logging.getLogger(">") # output pure log messages


    @classmethod
    def initialise(cls, is_test=True, level=logging.INFO):
        if not cls.initialised:
            logging.basicConfig(format='%(message)s', level=level)
            if os.environ.get("JENKINS_HOME", None) != None:
                ch = logging.StreamHandler()
                ch.setLevel(level)
                formatter = logging.Formatter('%(message)s')
                ch.setFormatter(formatter)
                cls.logger.addHandler(ch)

            cls.initialised = True
        return cls