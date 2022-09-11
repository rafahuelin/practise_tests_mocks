import requests
import responses
import unittest

from requests.exceptions import HTTPError, Timeout

from main import get_joke


class TestGetJokeWithResponses(unittest.TestCase):

    @responses.activate
    def test_get_joke_returns_joke(self):
        responses.get(
            url="http://api.icndb.com/jokes/random",
            json={"value": {"joke": "super funny joke"}},
            status=200
        )

        self.assertEqual(get_joke(), "super funny joke")

    @responses.activate
    def test_get_joke_raise_for_status(self):
        responses.get(
            url="http://api.icndb.com/jokes/random",
            json={"value": {"joke": "super funny joke"}},
            status=403
        )

        self.assertRaises(HTTPError, get_joke)

    @responses.activate
    def test_get_joke_timeout_error(self):
        responses.get(
            url="http://api.icndb.com/jokes/random",
            body=Timeout("Timeout reached")
        )

        self.assertEqual("No jokes because a timeout", get_joke())

    @responses.activate
    def test_get_joke_raises_general_exception(self):
        responses.get(
            url="http://api.icndb.com/jokes/random",
            # json={"value": {"joke": "super funny joke"}},
            body=Exception("General exception")
        )

        self.assertRaises(Exception, get_joke)


if __name__ == "__main__":
    unittest.main()
