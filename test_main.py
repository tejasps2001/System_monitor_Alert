#! /usr/bin/dev python3
#! python3

import unittest
import importlib
import subprocess

from main import install

class TestMain(unittest.TestCase):
    def test_dwnld_mdles(self):
            """Test whether third-party modules are correctly imported."""
            moduleName = 'pyinputplus'
            uninstall_cmd = f'pip uninstall {moduleName} -qy'
            subprocess.run(uninstall_cmd, shell=True)
            install(moduleName)
            # Check if moduleName is installed.
            self.assertTrue(importlib.import_module(moduleName))

unittest.main()