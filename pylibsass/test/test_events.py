import os

from pylibsass.events import FileSystemEvents

class TestFileSystemEvents():
    def _get_class(self, src="/test/test2/source", dest="/test/test2/dest"):
        return FileSystemEvents(src, dest)

    def _setup_tmpdir(self, tmpdir):
        src = tmpdir.mkdir("scss")
        src.join("test.scss").write(" ")
        src.join("test2.scss").write(" ")
        src.join("_test3.scss").write(" ")

        dest = tmpdir.mkdir("css")

        return src, dest

    def test_init(self):
        fs_events = self._get_class()

        assert fs_events._source_path == "/test/test2/source"
        assert fs_events._dest_path == "/test/test2/dest"

    def test_get_scss_files(self, tmpdir):
        src, dest = self._setup_tmpdir(tmpdir)
        fs_events = self._get_class(src=src.strpath, dest=dest.strpath)

        scss_files = fs_events.get_scss_files()

        assert set(scss_files) == set(["test.scss", "test2.scss"])

    def test_get_scss_files_partials(self, tmpdir):
        src, dest = self._setup_tmpdir(tmpdir)
        fs_events = self._get_class(src=src.strpath, dest=dest.strpath)

        scss_files = fs_events.get_scss_files(skip_partials=False)

        assert set(scss_files) == set(["test.scss", "test2.scss", "_test3.scss"])

    def test_get_scss_files_source_path(self, tmpdir):
        src, dest = self._setup_tmpdir(tmpdir)
        fs_events = self._get_class(src=src.strpath, dest=dest.strpath)

        scss_files = fs_events.get_scss_files(with_source_path=True)

        expected = map(lambda p: os.path.join(src.strpath, p), ["test.scss", "test2.scss"])

        assert set(scss_files) == set(expected)

    def test_get_scss_files_partials_source_path(self, tmpdir):
        src, dest = self._setup_tmpdir(tmpdir)
        fs_events = self._get_class(src=src.strpath, dest=dest.strpath)

        scss_files = fs_events.get_scss_files(skip_partials=False, with_source_path=True)

        expected = map(lambda p: os.path.join(src.strpath, p), ["test.scss", "test2.scss", "_test3.scss"])

        assert set(scss_files) == set(expected)
