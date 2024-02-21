import unittest
import glob

import main

class Test_getFilenameStringNoExtension(unittest.TestCase):
    def test1(self):
        self.assertEqual("testing", main.getFilenameStringNoExtension("testing.pdf"))
    def test2(self):
        self.assertEqual("dots.dots", main.getFilenameStringNoExtension("dots.dots.docx"))
    def test3(self):
        self.assertEqual("spaces in name", main.getFilenameStringNoExtension("spaces in name.pdf"))

class Test_clear_temp_files(unittest.TestCase):
    def test1(self):
        main.clear_temp_files()
        files = glob.glob('temp/*')
        self.assertEqual(0, len(files))


if __name__ == "__main__":
    unittest.main()