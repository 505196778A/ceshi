import yaml


def get_test_data(test_data_path):
    case = []
    http = []
    expected = []
    with open(test_data_path, "rb") as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat["tests"]
        for td in test:
            case.append(td.get("case", ""))
            http.append(td.get("http", {}))
            expected.append(td.get("expected", {}))
    parameters = zip(case, http, expected)
    return case, parameters


def get_sql(sql_path):
    with open(sql_path, "rb") as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        sql = dat["sql"]
    return sql

