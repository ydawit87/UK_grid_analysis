from utils.coordinates import coord_split


def test_coord_split_parses_coordinates():
    assert coord_split("1.2,2.3") == (1.2, 2.3)


def test_coord_split_preserves_none():
    assert coord_split(None) is None
