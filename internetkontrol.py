def checkInternetConnection():
    try:
        urlopen('https://google.com', timeout=3)
        return True
    except URLError as err:
        return False
    except KeyboardInterrupt:
        shutdown()

