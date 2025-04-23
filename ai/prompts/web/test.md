Generate Python UI test using Selene for: {description}

Requirements:
1. Use Page Object pattern
2. Add assertions with `should`
3. Include comments

Context:
{context}

Example:
'''python
def test_login_with_valid_credentials():
    (LoginPage()
     .open()
     .login("user", "pass")
     .assert_welcome_message_visible())
'''