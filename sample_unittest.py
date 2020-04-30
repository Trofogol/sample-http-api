import unittest, pymysql    # pymysql is imported for exception
from api import exec_mysql

class SampleTest(unittest.TestCase):
    def test_query(self):
        """
        check that query with correct syntax returns empty string
        and raises error when SQL syntax is incorrect
        """
        # correct query check
        request = 'SELECT * FROM offices WHERE name = "definetly not exists";'
        empty_answer = ()
        self.assertEqual (exec_mysql(request), empty_answer)
        
        # incorrect query (exception) check
        with self.assertRaises(pymysql.err.ProgrammingError):
            exec_mysql('SELUCT + FRUM offices WHAT? NAAH;')

if __name__ == '__main__':
    unittest.main()
