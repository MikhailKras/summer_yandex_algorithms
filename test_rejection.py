import unittest
from rejection import get_right_materials as get_mat


class TestGetMat(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(get_mat(
            ['LiTe', 'lite', 'bare', 'Bare'],
            ['Bare', 'BARE', 'Bear', 'bear', 'lite', 'Lite', 'LiTe', 'leti', 'leet', 'leto']
        ),
            'Bare bare   lite LiTe LiTe LiTe  LiTe')

    def test_case2(self):
        self.assertEqual(get_mat(
                ['DeLay'],
                ['delOy']
            ),
            'DeLay')


if __name__ == '__main__':
    unittest.main()
