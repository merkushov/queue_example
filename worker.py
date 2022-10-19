import time
import random
from redis import Redis

from settings import QUEUE_NAME

if __name__ == '__main__':
    r = Redis(host='queue', port=6379, db=0)

    while 1:
        message = r.rpop(QUEUE_NAME)

        if message:
            print(message)

        time.sleep(random.random())
