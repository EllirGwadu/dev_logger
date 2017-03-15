import unittest
import os
import sys

from LoggerDevelop import interfaceLog

class TestLoggerDevelop(unittest.TestCase):
    """Tests for LoggerDevelop"""

    def setUp(self):
        self.log_level = 'WARNING'

    def test_logging_message(self):
        while True:
            message = input('Enter some log message or q to exit: ')
            if 'q' in message:
                sys.exit()
            logg = interfaceLog(self.log_level, message)

unittest.main()