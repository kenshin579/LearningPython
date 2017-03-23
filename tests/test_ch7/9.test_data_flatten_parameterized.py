from unittest import TestCase

from nose.tools import assert_equal
from parameterized import parameterized

from ch7.data_flatten import flatten

class FlattenTestCase(TestCase):
    @parameterized.expand([
        ({'A': {'B': 'C', 'D': [1, 2, 3], 'E': {'F': 'G'}},
          'H': 3.14,
          'J': ['K', 'L'],
          'M': 'N'},
         {'A.B': 'C',
          'A.D': [1, 2, 3],
          'A.E.F': 'G',
          'H': 3.14,
          'J': ['K', 'L'],
          'M': 'N'}),
        (0, 0),
        ('Hello', 'Hello'),
        ({'A': None}, {'A': None}),
    ])
    def test_flatten(self, data, expected, prefix='', separator='.'):
        assert_equal(flatten(data, prefix=prefix, separator=separator), expected) #todo: 이게 잘 안됨

    '''
    test
    https://pypi.python.org/pypi/parameterized
    '''

    # @parameterized.expand([
    #     ("negative", -1.5, -2.0),
    #     ("integer", 1, 1.0),
    #     ("large fraction", 1.6, 1),
    # ])
    # def test_floor(self, name, input, expected):
    #     assert_equal(math.floor(input), expected)

    # test
    # @parameterized([
    #     (2, 2, 4),
    #     (2, 3, 8),
    #     (1, 9, 1),
    #     (0, 9, 0)
    # ])
    # def test_pow(base, exponent, expected):
    #     assert_equal(math.pow(base, exponent), expected)
