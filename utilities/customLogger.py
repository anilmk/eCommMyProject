import logging

class LogGen:
    # @staticmethod
    # def loggen1():
        # for handler in logging.root.handlers[:]:
        #     logging.root.removeHandler(handler)
        #     logging.basicConfig(filename='.\\logs\\automation.log',format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #     logger=logging.getLogger()
        #     logger.setLevel(logging.INFO)
        #     return logger

        # logger = logging.getLogger()
        # fhandler = logging.FileHandler(filename='.\\logs\\automation.log', mode='a')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fhandler.setFormatter(formatter)
        # logger.addHandler(fhandler)
        # logger.setLevel(logging.INFO)
        # return logger

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
            logging.basicConfig(filename='./logs/test_logs.log', format='%(asctime)s : %(levelname)s: %(message)s',
                            datefmt='%m %d %Y %I:%M:%S %p')
            logger = logging.getLogger()
            logger.setLevel(logging.INFO)
            return logger