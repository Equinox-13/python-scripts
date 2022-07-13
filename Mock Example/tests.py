import unittest
from main import add, substract
from unittest.mock import patch, MagicMock
from main import len_joke, get_joke


class TestAdd(unittest.TestCase):
    """
    Simple example using unittest
    """
    def test_add(self):
        self.assertEqual(add(2, 2), 4)

class TestSubstract(unittest.TestCase):
    """
    Simple example using unittest
    """
    def test_substract(self):
        self.assertEqual(substract(5, 3), 2)

class TestDivide(unittest.TestCase):
    """
    Mock divide() function as it takes time to execute
    """
    @patch('main.divide', return_value = 5)
    def test_divide(self, mock_divide):
        self.assertEqual(mock_divide(10, 2), 5)

class TestJoke(unittest.TestCase):

    @patch('main.get_joke')
    def test_len_joke(self, mock_get_joke):
        """
        The decorator patch creates a special fake object a MagicMock() object
        and passes the reference to it in to the decorated function
        The len_joke() function depends on the get_joke() function
        Each time we make a request we get a different joke so how can we test the
        len_joke() function?
        Here mocks will solve our problem
        mocks will help to isolate the len_joke() function that is under test from its dependency
        """
        mock_get_joke.return_value = 'one'
        self.assertEqual(len_joke(), 3)

    @patch('main.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value':{'joke': 'hello world'}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'hello world')

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=403)
        mock_response.json.return_value = {'value': {'joke': 'hello world'}}
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_joke(), 'No joke')


class TestBlog(unittest.TestCase):

    @patch('main.Blog')
    def test_posts(self, mock_blog):
        blog = mock_blog()
        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
                'body': 'Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.'
            }
        ]
        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)


if __name__ == '__main__':
    unittest.main()
