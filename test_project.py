import pytest
from project import create_platform_rects, change_col, game_over_screen


def test_create_platform_rects_output_type():
    output = create_platform_rects(3)
    assert isinstance(output, list)
    assert create_platform_rects(0) == []
    assert create_platform_rects(-6) == []

def test_create_platform_rects_output_length():
    assert len(create_platform_rects(3)) == 3
    assert len(create_platform_rects(5)) == 5
    assert len(create_platform_rects(0)) == 0
    assert len(create_platform_rects(2)[0]) == 4
    assert len(create_platform_rects(2)[1]) == 4


def test_create_platform_rects_errors():
    with pytest.raises(TypeError):
        create_platform_rects("r")
    with pytest.raises(TypeError):
        create_platform_rects()
    with pytest.raises(TypeError):
        create_platform_rects(1.5)
    with pytest.raises(TypeError):
        create_platform_rects([])


def test_game_over_screen_inputs():
    mock_list = [(180, 511, 33, 12), (200, 518, 33, 12), (45, 478, 75, 145)]
    assert game_over_screen(mock_list) == []
    assert len(game_over_screen(mock_list)) == 0
    assert game_over_screen([]) == []


def test_game_over_screen_errors():
    with pytest.raises(AttributeError):
        game_over_screen(1)
    with pytest.raises(AttributeError):
        game_over_screen("ds")
    with pytest.raises(AttributeError):
        game_over_screen(1.43)
    with pytest.raises(NameError):
        game_over_screen(ds)


def test_change_col():
    assert change_col(0) == (51, 255, 255)
    assert change_col(1) == (51, 255, 255)
    assert change_col(7) == (75, 0, 130)
    assert change_col(12) == (139, 0, 0)
    assert change_col(15) == (101, 67, 33)
    assert change_col(17) == (101, 67, 33)
    assert change_col(22) == (64, 64, 64)
    assert change_col(27) == (255, 0, 255)
    assert change_col(35) == (255, 0, 0)
    assert change_col(77) == (255, 0, 0)
    assert change_col(5.1) == (75, 0, 130)
    assert change_col(9.9) == (75, 0, 130)
    assert change_col(1000) == (255, 0, 0)


def test_change_col_errors():
    with pytest.raises(TypeError):
        change_col("fd")
    with pytest.raises(TypeError):
        change_col()
    with pytest.raises(TypeError):
        change_col([])



if __name__ == "__main__":
    pytest.main()