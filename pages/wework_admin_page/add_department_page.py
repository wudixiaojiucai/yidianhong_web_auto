from common.base import Base


class AddDepartmentPage(Base):
    _input_department_name = ("name", "name")  # 部门名称输入框
    _all_tips = ("id", "js_tips")  # 所有提示内容
    _belong_to_department = ("css selector", '.js_parent_party_name')  # 选择部门按钮
    _all_department = ("css selector", '.inputDlg_item a.jstree-anchor')  # 部门列表
    _save_btn = ("css selector", '[d_ck="submit"]')  # 确定按钮
    _cancel_btn = ("css selector", '[d_ck="cancel"]')  # 取消按钮

    def add_department_normal(self, department_name, belong_department_name):
        """输入部门名称"""
        self.send(self._input_department_name, department_name)
        """点击选择部门"""
        self.click(self._belong_to_department)
        """选择所属部门"""
        self.click_list_text(self._all_department, belong_department_name)
        self.click(self._save_btn)
        return self.get_text(self._all_tips)

    def add_department_fail_name(self, belong_department_name):
        """点击选择部门"""
        self.click(self._belong_to_department)
        """选择所属部门"""
        self.click_list_text(self._all_department, belong_department_name)
        self.click(self._save_btn)
        return self.get_text(self._all_tips)

    def add_department_fail_depart(self, department_name):
        """输入部门名称"""
        self.send(self._input_department_name, department_name)
        self.click(self._save_btn)
        return self.get_text(self._all_tips)
