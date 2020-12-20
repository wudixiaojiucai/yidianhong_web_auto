import os

top_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
cookie_file = os.path.join(top_path, "common", "cookie.yaml")

frame_contacts_yaml_path = os.path.join(top_path, "cases", "test_wework_admin_page", "frame_contacts.yaml")

if __name__ == '__main__':
    print(frame_contacts_yaml_path)
