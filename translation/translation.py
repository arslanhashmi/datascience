
import asyncio
import concurrent.futures
import logging
import sys
import time
import csv

MALE_STANDARD_NAME = 'abraham'
FEMALE_STANDARD_NAME = 'alaina'

sentence='MainThread run_blocking_tasks: waiting for executor tasks. arslan ayesha'

with open('dataSets/engWords.txt', 'r') as f: #just for reducing complexity
    englishWords = f.read()

with open('dataSets/maleNames.txt', 'r') as f:
    male = f.read()

with open('dataSets/femaleNames.txt', 'r') as f:
    female = f.read()

def find_in_male(word):
    if word in male:
        return 1
    return 0

def find_in_female(word):
    if word in female:
        return 1
    return 0

def eng_dict_checking(word):
    if word in englishWords:
        return 1
    return 0

def replaceMaleNames(maleNames):
    global sentence
    for names in maleNames:
        sentence = sentence.replace(names['male'][0],MALE_STANDARD_NAME)

def replaceFemaleNames(femaleNames):
    global sentence
    for names in femaleNames:
        sentence.replace(names['female'][0],FEMALE_STANDARD_NAME)

def blocks(n,word,index):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    if eng_dict_checking(word):
        log.info('done')
        #return {word:'N/A'}
        return 0
    else:
        if find_in_male(word):
            log.info('done')
            return {'male' : [word,index]}
        elif find_in_female(word):
            log.info('done')
            return {'female' : [word,index]}

    return 0

async def run_blocking_tasks(executor,wordList):

    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')

    log.info('creating executor tasks')
    loop = asyncio.get_event_loop()
    blocking_tasks = [
        loop.run_in_executor(executor, blocks, i,wordList[i].lower(),i)
        for i in range(len(wordList))
    ]
    log.info('waiting for executor tasks')
    completed, pending = await asyncio.wait(blocking_tasks)
    results = [t.result() for t in completed]
    refinedResults = [result for result in results if result!=0]
    maleNames = ([result for result in refinedResults if 'male' in result.keys()])
    femaleNames = ([result for result in refinedResults if 'female' in result.keys()])
    print (maleNames)
    print (femaleNames)
    replaceMaleNames(maleNames)
    replaceFemaleNames(femaleNames)
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

    print (sentence,'---')



