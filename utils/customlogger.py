import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()

        # FileHandler to log to file
        fhandler = logging.FileHandler(filename=r".\logs\test_log.log", mode="a")
        fhandler.setFormatter(logging.Formatter("(%asctime)s- %(name)s-%(levelname)s - %(message)s"))
        logger.addHandler(fhandler)

        # StreamHandler to log to console
        shandler = logging.StreamHandler()
        shandler.setFormatter(logging.Formatter("(%asctime)s- %(name)s-%(levelname)s - %(message)s"))
        logger.addHandler(shandler)

        # Set the logger level to INFO
        logger.setLevel(logging.INFO)

        return logger