import unittest
import testcases.test_search
import testcases.test_contact
import testcases.test_addtocart

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(testcases.test_search))
suite.addTests(loader.loadTestsFromModule(testcases.test_contact))
suite.addTests(loader.loadTestsFromModule(testcases.test_addtocart))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
