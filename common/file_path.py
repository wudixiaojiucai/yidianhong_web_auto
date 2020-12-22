import os
import yaml


def read_yaml(yaml_path):
    with open(yaml_path, encoding="utf-8") as f:
        res = f.read()
    content = yaml.safe_load(res)
    return content


top_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
cookie_file = os.path.join(top_path, "common", "cookie.yaml")

add_user_yaml_path = os.path.join(top_path, "cases", "test_wework_admin_page", "test_add_user",
                                  "add_user.yaml")

add_department_yaml_path = os.path.join(top_path, "cases", "test_wework_admin_page", "test_add_department",
                                        "add_department.yaml")

if __name__ == '__main__':
    print(read_yaml(add_department_yaml_path))
