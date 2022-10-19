An example of a distributed system built on queues.

* **scheduler.py** - puts tasks in a queue
* **worker.py** - Processes tasks that appear in the queue

Scaling is achieved by running more Workers

How to run the example
```bash
git clone ...
cd queue_example

docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
```