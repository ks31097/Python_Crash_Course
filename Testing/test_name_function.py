import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work correctly?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEquals(formatted_name, 'Janis Joplin')
    def test_first_middle_last_name(self):
        """Do names like Wolfgang Amadeus Mozart work correctly?"""
        # formatted_name = get_formatted_name('wolfgang', 'mozart', middle='amadeus')
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')

        self.assertEquals(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()