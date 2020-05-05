from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page

# Create your tests here.

class WikiTestCase(TestCase):
    def test_true_is_true(self):
        # """  if True is equal to True. Should always pass. '''
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a page """
        user = User()
        user.save()

        page = Page(title="My Test Page", content="test", author=user)
        page.save()
        #Make sure the slug that was generated in Page.save() matches what we think it should be
        self.assertEqual(page.slug, "my-test-page")

class PageListViewTests(TestCase):
    def test_multiple_pages(self):
        # Make some test data to be displayed on the page.
        user = User.objects.create()

        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="Another Test Page", content="test", author=user)

        # Issue a GET request to the MakeWiki homepage.
        # When we make a request, we get a response back.
        response = self.client.get('/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the number of pages passed to the template
        # matches the number of pages we have in the database.
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Page: My Test Page>', '<Page: Another Test Page>'],
            ordered=False
        )

        self.assertContains(response, "My Test Page")
        self.assertContains(response, "Another Test Page")

class PageDetailViewTests(TestCase):
    
    def test_detail_page(self):
        #set up the data
        user = User.objects.create()
        Page.objects.create(title="Pink Unicorns",
            content ="Unicorns dance on rainbows",
            author = user)

        #make a request
        response = self.client.get('/pink-unicorns/')

        #check the response
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Pink Unicorns")
        self.assertContains(response, "rainbows")
        self.assertContains(response, user)

