import threading
import time

def parallel_hisoblash(n):
    result = 0
    for i in range(n):
        result += i
    return result

def parallel_hisoblash_thread(n, thread_id):
    result = parallel_hisoblash(n)
    print(f"Thread {thread_id} natijasi: {result}")

def main():
    n = 10000000
    num_threads = 4

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=parallel_hisoblash_thread, args=(n // num_threads, i + 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Parallel hisoblash davomiyligi: {time.time() - start_time} soniya")
```

```python
import threading
import time

def parallel_hisoblash(n):
    result = 0
    for i in range(n):
        result += i
    return result

def parallel_hisoblash_thread(n, thread_id):
    result = parallel_hisoblash(n)
    print(f"Thread {thread_id} natijasi: {result}")

def main():
    n = 10000000
    num_threads = 4

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=parallel_hisoblash_thread, args=(n // num_threads, i + 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Parallel hisoblash davomiyligi: {time.time() - start_time} soniya")
