from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SnacksTestCase(TestCase):
    #Not using the hard coded path of the "Home page" in the urls.py file, but instead using the reverse() function
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    #using the hard coded path of the "Home page" in the urls.py file
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    #Not using the hard coded path of the "snack_list page" in the urls.py file, but instead using the reverse() function
    def test_snack_list_view_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    #using the hard coded path of the "snack_list page" in the urls.py file    
    def test_snack_list_page_status_code(self):
        response = self.client.get('/snack-list/')
        self.assertEqual(response.status_code, 200)

    def test_snack_detail_page_status_code_404(self):
        response = self.client.get('/snack-detail/100/')
        self.assertEqual(response.status_code, 404)

    #correct template used for the "Home page"
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    #correct template used for the "snack_list page"
    def test_snack_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')

    

    # def test_snack_detail_page_status_code_200(self):
    #     url = reverse('snack_detail', args=[1])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_snack_detail_page_template(self):
    #     url = reverse('snack_detail', args=[1])
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snack_detail.html')
    #     self.assertTemplateUsed(response, 'base.html')

    # def test_snack_detail_page_contents(self):
    #     url = reverse('snack_detail', args=[1])
    #     response = self.client.get(url)
    #     self.assertContains(response, 'Snack 1')
    #     self.assertContains(response, 'Snack 1 description')
    #     self.assertContains(response, 'Snack 1 calories')
    #     self.assertContains(response, 'Snack 1 sodium')
    #     self.assertContains(response, 'Snack 1 fat')
    #     self.assertContains(response, 'Snack 1 carbs')
    #     self.assertContains(response, 'Snack 1 protein')

    # def test_snack_list_page_contents(self):
    #     url = reverse('snack_list')
    #     response = self.client.get(url)
    #     self.assertContains(response, 'Snack 1')
    #     self.assertContains(response, 'Snack 1 description')
    #     self.assertContains(response, 'Snack 1 calories')


    
