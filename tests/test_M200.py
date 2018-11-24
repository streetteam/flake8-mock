def test_M200_called_once_found(flake8dir):
    flake8dir.make_example_py("""
        import unittest
        some_mock = unittest.mock.Mock()
        some_mock.called_once()
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:1: M200 called_once is a non-existent mock method",
    ]


def test_M200_called_once_not_found(flake8dir):
    flake8dir.make_example_py("""
        import unittest
        some_mock = unittest.mock.Mock()
        some_mock.assert_called_once()
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == []