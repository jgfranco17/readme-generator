import unittest
from generator.formats import Header
from generator.models import MarkdownGenerator


class TestGeneratorApp(unittest.TestCase):
    def setUp(self):
        self.app = MarkdownGenerator(config="config.yaml")
        self.h1 = Header(1, "Header 1")
        self.h2 = Header(2, "Header 2")
        self.h3 = Header(3, "Header 3")
        
    def test_headers(self):
        """
        Test the output of the header content.
        """
        self.assertEqual(self.h1.content, "# Header 1")
        self.assertEqual(self.h2.content, "## Header 2")
        self.assertEqual(self.h3.content, "### Header 3")
        
    def test_invalid_headers(self):
        invalid_config_file = "config.txt"
        with self.assertRaises(ValueError) as exception_context:
            failed_init = MarkdownGenerator(config=invalid_config_file)
            
        self.assertEqual(
            str(exception_context.exception),
            "A maximum of 10 fish can be added to the aquarium"
        )
        