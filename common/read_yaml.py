import yaml


def read_yaml(yaml_path):
    with open(yaml_path, encoding="utf-8") as f:
        res = f.read()
    content = yaml.safe_load(res)
    return content


if __name__ == '__main__':
    case_data = read_yaml("cookie.yaml")
    print(case_data)
