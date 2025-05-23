import pytest
import os

from utilities.readProperties import ReadConfig


class Test_003_Login_DDT():

    def test_003_login_DDT(self,browser_setup):
        self.driver= browser_setup()
        baseUrl= ReadConfig.get_url()
        self.driver(baseUrl)


        path = os.path.abspath(os.curdir)+"\\testData\\Login_DDT"











