import pytest

from human import Human


def test_human_grow():
    human = Human("John", 30, "male")
    human.grow()
    assert human.age == 31


def test_human_change_gender():
    human = Human("Jane", 25, "female")
    human.change_gender("male")
    assert human.gender == "male"


def test_human_change_gender_already_same():
    human = Human("Alice", 40, "female")
    with pytest.raises(Exception):
        human.change_gender("female")


def test_human_change_gender_invalid():
    human = Human("Bob", 35, "male")
    with pytest.raises(Exception):
        human.change_gender("invalid_gender")


def test_human_is_alive():
    human = Human("John", 30, "male")
    assert human.is_alive() == True


def test_human_is_alive_after_grow():
    human = Human("Jane", 80, "female")
    human.grow()
    assert human.is_alive() == True


def test_human_is_dead():
    human = Human("Alice", 100, "female")
    human.grow()
    assert human.is_alive() == False


def test_human_is_dead_after_change_gender():
    human = Human("Bob", 50, "male")
    human.change_gender("female")
    assert human.is_alive() == False


def test_human_initial_status_alive():
    human = Human("John", 30, "male")
    assert human.is_alive() == True


def test_human_initial_status_dead():
    human = Human("Jane", 110, "female")
    assert human.is_alive() == False


def test_human_grow_beyond_age_limit():
    human = Human("Alice", 99, "female")
    human.grow()
    assert human.is_alive() == True
    human.grow()
    assert human.is_alive() == False


def test_human_change_gender_same():
    human = Human("Bob", 35, "male")
    with pytest.raises(Exception):
        human.change_gender("male")


def test_human_change_gender_invalid():
    human = Human("Eve", 45, "female")
    with pytest.raises(Exception):
        human.change_gender("other")


def test_human_age_property():
    human = Human("Sam", 50, "male")
    assert human.age == 50
    human.grow()
    assert human.age == 51


def test_human_gender_property():
    human = Human("Alex", 25, "female")
    assert human.gender == "female"
    human.change_gender("male")
    assert human.gender == "male"


if __name__ == "__main__":
    pytest.main()
