from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome(executable_path ="your chrome driver path")

def main():
	global browser
	#browser.set_window_position(-3000,0)
	browser.get('http://twitter.com/login')
	print "[+] Accessing twitter ........."
	twitter()
	addme_like()

def twitter():
	user = browser.find_element_by_css_selector('.js-username-field')
	user.send_keys('your Username')
	sleep(2)
	passw = browser.find_element_by_css_selector('.js-password-field')
	passw.send_keys('Your password')
	sub = browser.find_element_by_css_selector('button.submit')
	sub.click()
	print "[+]Logged in Successfully into twitter"
	addme_login()


def addme_login():
	print "\n\n[*] Accessing AddMeFast"
	browser.get('http://addmefast.com')
	sleep(4)
	user = browser.find_element_by_css_selector('.email')
	email = 'your Email'
	user.send_keys(email)
	passw = browser.find_element_by_css_selector('.password')
	passw.send_keys('Your Password')
	sub = browser.find_element_by_css_selector('li.last > input:nth-child(1)')
	sub.click()
	print "Logged in Successfully into AddMeFast As : {}".format(email)
	browser.set_window_position(-3000,0)


def addme_like():
	try:
		for i in range(1,200):
			browser.get('http://addmefast.com/free_points/twitter')
			sleep(5)
			points()
			browser.execute_script("document.querySelector('.single_like_button').click()")
			browser.switch_to_window(browser.window_handles[1])
			sleep(4)
			try:
				like = browser.find_element_by_css_selector('button.button:nth-child(5)')
				print "\n[*]you liked that twitter"
				like.click()
				sleep(4)
			except Exception:
				sleep(3)
				browser.close()
				browser.switch_to_window(browser.window_handles[0])
				addme_like()
			browser.close()
			print "\n[*] Window is closed"
			browser.switch_to_window(browser.window_handles[0])
			sleep(3)
			browser.current_url
	except Exception:
		print "Retrying ........"
		browser.switch_to_window(browser.window_handles[0])
		sleep(2)
		addme_like()

def points():
	point = browser.find_element_by_css_selector('body > div.wrapper > div:nth-child(1) > section > div > div > div.head-welcome > span')
	point = point.get_attribute("outerHTML")
	point = point.replace('<span class="points_count">','')
	point = point.replace('</span>','')
	print "\n[*] The total points are : {}".format(point)


if __name__ == '__main__':
	main()
