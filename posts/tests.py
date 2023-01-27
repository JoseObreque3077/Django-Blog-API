from django.contrib.auth import get_user_model
from django.test import TestCase

from posts.models import Post


class BlogTests(TestCase):
    """
    Test class for the 'Post' model.

    This test class extends the functionality of the Django's 'TestCase' class.
    It contains unit tests that ensure the 'Post' model functions correctly,
    data are properly stored and retrieved from the database.
    """
    @classmethod
    def setUpTestData(cls):
        """
        A method that runs before all test methods in the class and sets up test
        data that all the test will use.
        """
        user_model = get_user_model()
        cls.user = user_model.objects.create_user(
            username='test_user',
            email='test@example.net',
            password='test_pass',
            name='Test User'
        )

        cls.post = Post.objects.create(
            title='Test Post',
            body='Test Content',
            author=cls.user
        )

    def test_post_model(self):
        """
        A test method that checks whether the stored 'Post' object contains the
        correct field values and string representation.
        """
        # Checks that the created post has the right data
        self.assertEqual(
            first=self.post.title,
            second='Test Post'
        )
        self.assertEqual(
            first=self.post.body,
            second='Test Content'
        )
        self.assertEqual(
            first=self.post.author,
            second=self.user
        )
        self.assertEqual(
            first=self.post.created_at,
            second=self.post.updated_at
        )

        # Checks that the created post has the right string representation
        self.assertEqual(
            first=str(self.post),
            second='Test Post'
        )
