import time

def wait_interval(rate_per_minute):
    """Wait based on the rate per minute"""
    if rate_per_minute > 0:
        interval = 60 / rate_per_minute
        time.sleep(interval)
    else:
        time.sleep(1)  # default wait if invalid rate
