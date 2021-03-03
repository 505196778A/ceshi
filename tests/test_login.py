import pytest
import requests
from utils.commonlib import get_test_data
import allure


cases, parameters = get_test_data("./data/login.yaml")


@allure.feature("测试登录接口")
class TestLogin(object):
    @pytest.mark.parametrize("case,http,expected", list(parameters), ids=cases)
    def test_login(self, env, case, http, expected):
        r = requests.request(method=http["method"], url=env + http["path"], headers=http["headers"],
                             data=http["data"])
        response = r.json()
        print(response)
        assert response["msg"] == expected["response"]["msg"]
        assert response["code"] == expected["response"]["code"]
