import unittest

import widget_svm


class Widget_svmTestCase(unittest.TestCase):

    def setUp(self):
        self.app = widget_svm.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to widget_svm', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
