from django.test import TestCase

# Create your tests here.

class HomepageTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/')
	def test_get(self):
		#get / must return 200
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):		
		self.assertTemplateUsed(self.resp, 'index.html')
