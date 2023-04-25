#! /usr/bin/dev python3
#! python3

import sys
from main import install
import subprocess
import unittest

class TestMain(unittest.TestCase):
    def test_dwnld_mdles(self):
        """Test whether third-party modules are correctly imported."""
        moduleName = 'ezsheets'
        uninstall_cmd = f'pip uninstall {moduleName} -qy'
        uninstall = subprocess.run(uninstall_cmd, shell=True)
        install(moduleName)
        self.assertIsNotNone(moduleName)

unittest.main()