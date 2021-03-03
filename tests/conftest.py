import os
import yaml
import pytest
from utils.commonlib import get_test_data
import requests


@pytest.fixture(scope="session")
def env(request):
    config_path = os.path.join(str(request.config.rootdir),
                               "config",
                               "test",
                               "host.yaml")
    with open(config_path, "rb") as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
        host_path = env_config["host"]["shequ"]
    return host_path


cases, parameters = get_test_data("./data/login_token.yaml")
list_parameters = list(parameters)


@pytest.fixture(scope="session")
def get_token(env):
    r = requests.request(method=list_parameters[0][1]["method"], url=env+list_parameters[0][1]["path"],
                         data=list_parameters[0][1]["data"], headers=list_parameters[0][1]["headers"])
    response = r.json()
    header = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
               "token": response["data"]["token"]}
    return header

