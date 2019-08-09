import requests

def test_t():
    count = 0
    while count < 5:
        print("sleep", count)
        sleep(count)
        assert True
