import unittest
from Tests.test_login import TestLogin

login_test = unittest.TestLoader().loadTestsFromTestCase(TestLogin)

test_suite = unittest.TestSuite([login_test])

unittest.TextTestRunner(verbosity=2).run(test_suite)
