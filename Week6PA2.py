import multiprocessing
import time
import random
from datetime import datetime

def worker():
    # Generate a random sleep time between 0 and 1 second
    sleep_time = random.uniform(0, 1)
    time.sleep(sleep_time)
    
    # Get the current time and print it
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Process {multiprocessing.current_process().name} - Current Time: {current_time}")
    
if __name__ == "__main__":
    # Create three separate processes
    processes = [multiprocessing.Process(target=worker, name=f"Process-{i+1}") for i in range(3)]

    # Start each process
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")