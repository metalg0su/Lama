from time import sleep
import requests

def test_t():
    count = 0
    while count < 5:
        print("sleep", count)
        sleep(count)
        count += 1
        assert True
