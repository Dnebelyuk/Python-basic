"""
Необходимо создать два параллельных потока, каждый из которых выводил бы на экран числа от 10 до 1
в обратном порядке с интервалом в одну секунду. В выводе должно быть понятно какая
нить выполняется, и когда каждая из них начинает и заканчивает своё выполнение.
"""

import threading
import time


def countdown(thread):
    print(f"{thread}: начал выполнение")
    for i in range(10, 0, -1):
        print(f"{thread}: {i}")
        time.sleep(1)
    print(f"{thread}: завершил выполнение")


thread1 = threading.Thread(target=countdown, args=("Поток 1",))
thread2 = threading.Thread(target=countdown, args=("Поток 2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

