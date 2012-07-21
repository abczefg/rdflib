import unittest

from rdflib.term import Literal

from rdflib.store import NodePickler

try:
    from literals import cases
except: 
    from test.literals import cases


class UtilTestCase(unittest.TestCase):

    def test_to_bits_from_bits_round_trip(self):
        np = NodePickler()

        a = Literal(u'''A test with a \\n (backslash n), "\u00a9" , and newline \n and a second line.
''')
        b = np.loads(np.dumps(a))
        self.assertEquals(a, b)

    def test_literal_cases(self): 
        np = NodePickler()

        for l in cases: 
            a = Literal(l)
            b = np.loads(np.dumps(a))
            self.assertEquals(a, b)
        

if __name__ == '__main__':
    unittest.main()