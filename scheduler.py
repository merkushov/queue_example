from redis import Redis
from settings import QUEUE_NAME

if __name__ == '__main__':
    r = Redis(host='queue', port=6379, db=0)

    for i in range(1000):
        r.lpush(QUEUE_NAME, f"account_id {i}")
