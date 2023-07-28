import pytest

from human import Human


def test_human_grow():
    human = Human("John", 30, "male")
    human.grow()
    assert human.age == 31, "Age is changed to 1"


def test_human_change_gender():
    human = Human("Jane", 25, "female")
    human.change_gender("male")
    assert human.gender == "male", "Gender is not changed"


def test_human_age_property():
    human = Human("Sam", 50, "male")
    assert human.age == 50, "Human age is not 50, parameters parsed wrong"
    human.grow()
    assert human.age == 51, "Human does not grow"


def test_human_gender_property():
    human = Human("Alex", 25, "female")
    assert human.gender == "female", "parameters parsed wrong"
    human.change_gender("male")
    assert human.gender == "male", "Gender is not changed"


def test_human_grow_1():
    human = Human("John", 30, "male")
    human.grow()
    assert human.age == 31, "Age is not incremented by 1 after calling grow()"


def test_human_change_gender_1():
    human = Human("Jane", 25, "female")
    human.change_gender("male")
    assert human.gender == "male", "Gender is not changed to 'male' after calling change_gender()"


def test_human_change_gender_already_same():
    human = Human("Alice", 40, "female")
    with pytest.raises(Exception):
        human.change_gender("female"), "Exception is not raised when changing to the same gender"
    assert human.gender == "female", "Gender is changed even when attempting to set the same gender"


def test_human_change_gender_invalid():
    human = Human("Bob", 35, "male")
    with pytest.raises(Exception):
        human.change_gender("invalid_gender"), "Exception is not raised when changing to an invalid gender"
    assert 'invalid_gender' != 'male' or 'female', 'Not available Gender'


def test_human_age_property_1():
    human = Human("Sam", 50, "male")
    assert human.age == 50, "Age property does not return the correct initial age"
    human.grow()
    assert human.age == 51, "Age property does not reflect the incremented age after calling grow()"


def test_human_dead():
    human = Human("Gordon", 100, "male")
    human.grow()
    assert human.age == 100, "The age is increased, 100 the biggest Age for Human class"

