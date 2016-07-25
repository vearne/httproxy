import time
import threading


class Counter(object):
    def __init__(self):
        self.curr = 0
        self.internal_dd = {}
        self.lock = threading.Lock()

    def increment(self, key):
        t = int(time.time())
        sign = t / 60

        # lock
        self.lock.acquire()
        try:
            if sign != self.curr:
                self.curr = sign
                self.internal_dd = {}

            if key not in self.internal_dd:
                self.internal_dd[key] = 0

            self.internal_dd[key] += 1

            # unlock
            return self.internal_dd.get(key, 0)
        finally:
            self.lock.release()


if __name__ == '__main__':
    c = Counter()
    for i in range(100):
        time.sleep(0.2)
        x = c.increment('hello')
        if x > 50:
            print "over limit"
        print x
        print c.internal_dd
