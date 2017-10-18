'''from threading import Thread
import asyncio
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
import time
def more_work(x):
  print("More work %s" % x)
  time.sleep(x)
  print("Finished more work %s" % x)
async def do_some_work(x):
  print("some work %s" % x)
  time.sleep(x)
  print("Finished some work %s" % x)
#new_loop.call_soon_threadsafe(more_work, 20)
asyncio.run_coroutine_threadsafe(do_some_work(5), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(10), new_loop)'''

import asyncio
import concurrent.futures
import logging
import sys
import time
import csv

sentence='MainThread run_blocking_tasks: waiting for executor tasks.'

with open('dataSets/engWords.txt', 'r') as f:
    englishWords = f.read()

file=open( "dataSets/Indian-Female-Names.csv", "r",encoding='utf-8')
female = csv.reader(file)
file=open( "dataSets/Indian-Male-Names.csv", "r",encoding='utf-8')
male = csv.reader(file)


def find_in_male(word):
    pass

def find_in_female(word):
    for line in female:
        if line[0] == word:
            print(line)


def blocks(n,word):
    if word in englishWords:
        return {word : 'N/A'}
    else:
        if find_in_male(word):
            return {word : 'male'}
        elif find_in_female(word):
            return {word : 'female'}
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    log.info('done')
    return {}


async def run_blocking_tasks(executor,wordList):

    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor, blocks, i,wordList[i].lower())
        for i in range(len(wordList))
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    print (results)
    log.info('results: {!r}'.format(results))

    log.info('exiting')


if __name__ == '__main__':
    # Configure logging to show the name of the thread
    # where the log message originates.
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # Create a limited thread pool.
    executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=len(sentence.split(' ')),
    )

    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(
            run_blocking_tasks(executor,sentence.split(' '))
        )
    finally:
        event_loop.close()