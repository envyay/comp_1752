from library_item import LibraryItem
import pytest


@pytest.fixture
def sample_item():
    return LibraryItem(name="Another Brick in the Wall", artist="Pink Floyd", rating=3, artist_image="")


def test_initialization_default_values():
    item = LibraryItem(name="Stayin' Alive", artist="Bee Gees", artist_image="")
    assert item.name == "Stayin' Alive"
    assert item.artist == "Bee Gees"
    assert item.rating == 0
    assert item.play_count == 0


def test_initialization_custom_values(sample_item):
    assert sample_item.name == "Another Brick in the Wall"
    assert sample_item.artist == "Pink Floyd"
    assert sample_item.rating == 3
    assert sample_item.play_count == 0


def test_info_with_stars(sample_item):
    expected_info = "Another Brick in the Wall - Pink Floyd ***"
    assert sample_item.info() == expected_info


def test_stars_method(sample_item):
    assert sample_item.stars() == "***"

    sample_item.rating = 5
    assert sample_item.stars() == "*****"

    sample_item.rating = 0
    assert sample_item.stars() == ""


def test_play_count_increment(sample_item):
    assert sample_item.play_count == 0

    sample_item.play_count += 1
    assert sample_item.play_count == 1

    sample_item.play_count += 2
    assert sample_item.play_count == 3