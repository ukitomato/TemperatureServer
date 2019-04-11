import time

from lib import dht11
from lib.thingspeak import send_data

ERROR_LIMIT = 25

STATUS_NORMAL = 0
STATUS_WARNING = 1


class Dht:
    def __init__(self):
        self.humidity = None
        self.temperature = None
        self.cron = False
        self.interval = 60
        self.status = STATUS_WARNING

    # 更新
    def update(self):
        self.status = STATUS_WARNING

        result = dht11.read_dht11_dat()

        if result:
            self.humidity, self.temperature = result
            self.status = STATUS_NORMAL
            return result
        else:
            return False

    # 定期更新
    def cron_start(self, interval=60):
        self.interval = interval
        self.cron = True
        while self.cron:
            if self.update():
                send_data(self.temperature, self.humidity)
                time.sleep(self.interval)

    def cron_stop(self):
        self.cron = False

    def set_interval(self, interval):
        self.interval = interval

    def destroy(self):
        dht11.destroy()
