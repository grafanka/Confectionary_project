import unittest
import test_discount

loader = unittest.TestLoader()
runner = unittest.TextTestRunner(verbosity=2)


suite_select_discount = loader.loadTestsFromTestCase(test_discount.TestSelectionDiscount)
suite_calculation_discount = loader.loadTestsFromTestCase(test_discount.TestCalculationDiscount)



result_1 = runner.run(suite_select_discount)
result_2 = runner.run(suite_calculation_discount)
