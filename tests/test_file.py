from pathlib import Path

from lamindb.dev._core import get_name_suffix_from_filepath


def test_get_name_suffix_from_filepath():
    # based on https://stackoverflow.com/questions/31890341/clean-way-to-get-the-true-stem-of-a-path-object  # noqa
    dataset = [
        ("a", "a", ""),
        ("a.txt", "a", ".txt"),
        ("archive.tar.gz", "archive", ".tar.gz"),
        ("directory/file", "file", ""),
        ("d.x.y.z/f.a.b.c", "f", ".a.b.c"),
        ("logs/date.log.txt", "date", ".txt"),
    ]
    for path, name, suffix in dataset:
        filepath = Path(path)
        assert name, suffix == get_name_suffix_from_filepath(filepath)