import unittest
import coverage
from test_helpers import setup_test_environment, teardown_test_environment

def run_all_tests():
    # Start coverage tracking
    cov = coverage.Coverage()
    cov.start()
    
    # Setup test environment
    setup_test_environment()
    
    # Discover and run tests
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    
    # Stop coverage tracking and generate reports
    cov.stop()
    cov.save()
    
    # Generate coverage reports
    print('\nCoverage Report:')
    cov.report()
    cov.html_report(directory='coverage_html')
    cov.xml_report(outfile='coverage.xml')
    
    # Cleanup test environment
    teardown_test_environment()

if __name__ == '__main__':
    run_all_tests() 