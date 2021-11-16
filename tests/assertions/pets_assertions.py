from assertpy import assert_that


def assert_pet_name_exists(response, pet_name):
    assert_that(response.as_dict).is_not_empty().contains(pet_name)


def assert_add_new_pet_is_successful(response, first_name):
    assert_that(response.as_dict).extracting('fname').is_not_empty().contains(first_name)
