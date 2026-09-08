from  page.startapp import StartAPP
class Test_PasswordLogin:
    def test_userNull(self):
        StartAPP().start().goto_safe().goto_home().goto_login().goto_password_login().user_input().password_input("xxxxxxxxxx").user_protocal().login_fail()
    def test_pwdNull(self):
        StartAPP().start().goto_safe().goto_home().goto_login().goto_password_login().user_input("178xxxxxxxxxx").password_input().user_protocal().login_fail()
    def test_protocalNull(self):
        StartAPP().start().goto_safe().goto_home().goto_login().goto_password_login().user_input("178xxxxxxxxxx").password_input("xxxxxxxxxx").login_fail()
    def test_loginSuccesss(self):
        StartAPP().start().goto_safe().goto_home().goto_login().goto_password_login().user_input("178xxxxxxxxxx").password_input("xxxxxxxxxx").user_protocal().login_success()
class Test_CodeLogin:
    pass