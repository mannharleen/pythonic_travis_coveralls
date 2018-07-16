import logging

logger = logging.getLogger('module1')
h = logging.StreamHandler()
h.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(name)s | %(message)s'))
logger.addHandler(h)
logger.setLevel(logging.INFO)
logger.info('logging info at module level')


class C1:
    def __init__(self, value):
        logger = logging.getLogger('module1_c1_init')
        logger.addHandler(h)
        logger.setLevel(logging.WARNING)
        logger.warning('logging warn for class c1 init method')
        self.value = value

    def __call__(self, *args, **kwargs):
        logger = logging.getLogger('module1_c1_call')
        logger.addHandler(h)
        logger.setLevel(logging.WARNING)
        logger.warning('logging warn for class c1 call method')
        return 2


if __name__ == '__main__':
    o1 = C1(1)
    o1()
