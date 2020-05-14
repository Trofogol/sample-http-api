import unittest, pymysql    # pymysql is imported for exception
import api

class SampleTest(unittest.TestCase):
    def test_query(self):
        """
        check that query with correct syntax returns empty string
        and raises error when SQL syntax is incorrect
        """
        # correct query check
        request = 'SELECT * FROM offices WHERE name = "definetly not exists";'
        empty_answer = ()
        # expect empty answer w/o any errors
        self.assertEqual (api.exec_mysql(request), empty_answer)
        
        # incorrect query (exception) check
        with self.assertRaises(pymysql.err.ProgrammingError):  # (expect error when SQL syntax is violated)
            api.exec_mysql('SELUCT + FRUM offices WHAT? NAAH;')

if __name__ == '__main__':
    unittest.main()
