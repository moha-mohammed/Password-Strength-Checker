from checker import check_password_strength

def test_common_password():
    assert "Very Weak" in check_password_strength("password")

def test_strong_password():
    assert "Strong" in check_password_strength("P@ssw0rd123!")

def test_weak_password():
    assert "Weak" in check_password_strength("abc")
