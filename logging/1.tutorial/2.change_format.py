# myapp.py
import logging


def main():
    # Changing the format of displayed messages
    # logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    # logging.basicConfig(format='%(asctime)s %(message)s')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')


if __name__ == '__main__':
    main()
