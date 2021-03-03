import pytest
import requests
from utils.commonlib import get_test_data, get_sql
import allure
from utils.mysql_db import HandleMySql


cases, parameters = get_test_data("./data/gonggao.yaml")
Mysql = HandleMySql()


@allure.feature("测试公告接口")
class TestLogin(object):
    @pytest.mark.parametrize("case,http,expected", list(parameters), ids=cases)
    def test_login(self, env, get_token, case, http, expected):
        r = requests.request(method=http["method"], url=env + http["path"], headers=get_token,
                             data=http["data"])
        response = r.json()
        print(response)
        assert response["msg"] == expected["response"]["msg"]
        assert response["code"] == expected["response"]["code"]
        sql = str(get_sql("./sql/fabugonggao_sql.yaml"))
        single_data = Mysql.get_value(sql, is_more=True)
        print(single_data)