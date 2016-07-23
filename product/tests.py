from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class FirefoxTestCase(TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.addCleanup(self.browser.quit)

	def testPageTitle(self):
		self.browser.get('http://127.0.0.1:8000/')
		self.assertIn('Sentiment |', self.browser.title)

if __name__ == '__main__':
	unittest.main(verbosity=2)