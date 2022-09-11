import responses
import unittest

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


if __name__ == "__main__":
    unittest.main()
