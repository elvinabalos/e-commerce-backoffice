import pytest

# ===================
# POSITIVE TEST
# ===================
def test_login_success(login_page, test_data):
    login_page.login(
        test_data["admin"]["username"],
        test_data["admin"]["password"]
    )
    login_page.assert_login_success()
    login_page.logout()


# ===================
# NEGATIVE TESTS
# ===================
@pytest.mark.parametrize("username,password", [
    ("superadmin", "wrongpass"),      # wrong password
    ("wronguser", "superadmin031819"),# wrong username
    ("", "superadmin031819"),         # empty username
    ("superadmin", ""),                # empty password
    ("", ""),                          # both empty
])
def test_login_negative(login_page, username, password):
    login_page.login(username, password)
    login_page.assert_login_failed()

# ===================
# EDGE CASES
# ===================
@pytest.mark.parametrize("username,password", [
    # (" superadmin ", "superadmin031819"),      # leading/trailing space
    # ("SUPERADMIN", "superadmin031819"),        # case sensitivity
    ("superadmin", "SUPERADMIN031819"),        # case password
    ("!"*256, "superadmin031819"),             # very long username
    ("superadmin", "!"*256),                   # very long password
    ("<script>alert(1)</script>", "superadmin031819"),  # XSS injection
])
def test_login_edge_cases(login_page, username, password):
    login_page.login(username, password)
    login_page.assert_login_failed()