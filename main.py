import crawl
import utils
import time

USER = 'uwealthed'
PASS = 'P@ss2322'

FILE = 'Code1.txt'

list_of_captcha = utils.get_captcha(FILE)


crawl.init()
crawl.login_cred(USER, PASS)
crawl.go_to_captcha()
while True:
    crawl.crawl_captcha(list_of_captcha)
    print("========Pause=========")
    time.sleep(15) # seconds
