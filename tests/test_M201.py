def test_M201_called_once_found(flake8dir):
    flake8dir.make_example_py("""
        import unittest
        some_mock = unittest.mock.Mock()
        assert some_mock.called_once
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == [
        "./example.py:3:1: M201 called_once is a non-existent mock property",
    ]


def test_M201_called_once_not_found(flake8dir):
    flake8dir.make_example_py("""
        import unittest
        some_mock = unittest.mock.Mock()
        some_mock.assert_called_once()
    """)
    result = flake8dir.run_flake8()
    assert result.out_lines == []