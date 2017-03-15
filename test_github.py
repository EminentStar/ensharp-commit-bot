import unittest
import datetime


from github import github_date_to_localtime
from github import is_today
from github import did_commit_today


class TestGithub(unittest.TestCase):
    def setUp(self):
        self.sample_date = datetime.datetime(1991, 11, 24, 18, 2, 36)
    def test_github_date_to_localtime(self):
        date_str = '2016-11-24T09:02:36Z'
        expected = datetime.datetime(2016, 11, 24, 18, 2, 36)
        actual = github_date_to_localtime(date_str)
        self.assertTrue(expected, actual)

    def test_is_today(self):
        expected_1 = True
        actual_1 = is_today(self.sample_date)

        self.assertTrue(expected_1, actual_1)
    
    def test_did_commit_today(self):
        input = '1991-03-02T06:47:43Z'
        expected = False
        actual = did_commit_today(input)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
