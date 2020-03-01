import subprocess
from contextlib import contextmanager
import datetime

@contextmanager
def estime(app_name):
    try:
        time_begin = datetime.datetime.now()
        subprocess.call(["python", app_name])
        time_end = datetime.datetime.now()
        time_diff = time_end - time_begin
        print(f'Test app start time: {time_begin}')
        print(f'Test app completion time: {time_end}')
        print(f'Test app run time: {time_diff}')
        yield [time_begin, time_end, time_diff]
    finally:
        pass


with estime("test_app.py") as estime_result:
    pass