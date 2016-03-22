'''
Integration test case for say hi command

@author:luzC
'''
import subprocess

from demo_tempest_plugin.tests.api import base
from tempest import test


class TestSayHiInt(base.BaseSayHi):

    @classmethod
    def resource_setup(cls):
        super(TestSayHiInt, cls).resource_setup()

    @test.attr(type="smoke")
    def test_hi(self):
        # Run dluxsay command
        result = subprocess.Popen("dluxsay personA", shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.assertIn('personA', result.stdout.read())

    @classmethod
    def resource_cleanup(cls):
        super(TestSayHiInt, cls).resource_cleanup()

