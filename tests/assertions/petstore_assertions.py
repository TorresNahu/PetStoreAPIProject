from assertpy import assert_that


def assert_add_new_pet_is_successful(response, excepted_pet_id):
    assert_that(response.as_dict['id']).is_equal_to(excepted_pet_id)


def assert_updated_pet_name(response, expected_pet_name):
    assert_that(response.as_dict['name']).is_equal_to(expected_pet_name)


def assert_response_status_code_is_valid(response, expected_status_code):
    assert_that(response.status_code).is_equal_to(expected_status_code)


def assert_create_new_user_is_successful(response, expected_username):
    assert_that(response.as_dict['username']).is_equal_to(expected_username)
