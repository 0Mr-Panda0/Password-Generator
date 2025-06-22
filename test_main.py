from pass_gen.password_generator import creating_password
from pass_gen.database_conn import (
    insert_password,
    get_last_password,
    delete_last_password,
    create_table,
)
from string import digits, ascii_letters, punctuation


def test_creating_password_with_special_characters():
    # Test with special characters allowed
    password = creating_password(12, "Yes")
    assert len(password) == 12
    assert any(char in punctuation for char in password), (
        "Password should contain special characters"
    )


def test_creating_password_without_special_characters():
    # Test without special characters
    password = creating_password(12, "No")
    assert len(password) == 12
    assert not any(char in punctuation for char in password), (
        "Password should not contain special characters"
    )


def test_creating_password_with_minimum_length():
    # Test with minimum length
    password = creating_password(1, "Yes")
    assert len(password) == 1


def test_creating_password_with_maximum_length():
    # Test with maximum length
    password = creating_password(100, "Yes")
    assert len(password) == 100
    assert any(char in punctuation for char in password), (
        "Password should contain special characters"
    )
    assert all(char in (digits + ascii_letters + punctuation) for char in password), (
        "Password contains invalid characters"
    )


def test_creating_password_with_edge_cases():
    # Test with empty length
    password = creating_password(0, "Yes")
    assert len(password) == 0, "Password should be empty for length 0"


def test_insert_password():
    # Test inserting password into the database
    # Ensure the table is created
    create_table()
    # Insert a test password
    # Note: This is a simple test and should be isolated from other tests
    test_password = "TestPassword123!"
    insert_password(test_password)

    # Retrieve the last password from the database
    last_password = get_last_password()

    assert last_password == test_password, (
        "Inserted password does not match the retrieved password"
    )

    delete_last_password()
