import unittest
from request import Request


class TestRequest(unittest.TestCase):
    """
    Test Request serialization
    """
    def test_init(self):
        data = {
            "object_kind": "object_kind",
            "event_name": "event_name",
            "user_name": "user_name",
            "user_username": "user_username",
            "project": "project",
            "repository": "repository",
            "homepage": "homepage",
            "commits": "commits"
        }

        request = Request(data)

        self.assertEqual(request.object_kind, "object_kind")
        self.assertEqual(request.event_name, "event_name")
        self.assertEqual(request.user_name, "user_name")
        self.assertEqual(request.user_username, "user_username")
        self.assertEqual(request.project, "project")
        self.assertEqual(request.repository, "repository")
        self.assertEqual(request.homepage, "homepage")
        self.assertEqual(request.commits, "commits")


if __name__ == '__main__':
    unittest.main()
