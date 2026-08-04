import time
def start(sec):
    for i in range(sec):
        print(f'Elapsed: {i+1}s')
        time.sleep(0.1)