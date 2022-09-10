import unittest
from unittest.mock import patch

from main import len_joke


class TestAdd(unittest.TestCase):

    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "hello"
        self.assertEqual(len_joke(), 5)


if __name__ == "__main__":
    unittest.main()
