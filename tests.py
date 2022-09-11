import requests
import unittest
from requests.exceptions import HTTPError, Timeout
from unittest.mock import patch, MagicMock

from main import get_joke, len_joke


class TestJoke(unittest.TestCase):

    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "hello"
        self.assertEqual(len_joke(), 5)

    @patch("main.requests")
    def test_get_joke(self, mock_requests):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "value": {"joke": "hello world"}
        }

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "hello world")

    @patch("main.requests")
    def test_get_joke_fails(self, mock_requests):
        mock_response = MagicMock(status_code=400)
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No jokes")

    @patch("main.requests")
    def test_get_joke_timeout_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout("The server is taking its time...")

        self.assertEqual(get_joke(), "No jokes because a timeout")

    @patch("main.requests")
    def test_get_joke_raise_for_status(self, mock_request):
        mock_response = MagicMock(status_code=400)
        mock_response.raise_for_status.side_effect = HTTPError("Something goes wrong")

        mock_request.exceptions = requests.exceptions
        mock_request.get.return_value = mock_response

        self.assertRaises(HTTPError, get_joke)

        with self.assertRaises(HTTPError) as ctx:
            get_joke()

        self.assertEqual(str(ctx.exception), "Something goes wrong")


if __name__ == "__main__":
    unittest.main()
