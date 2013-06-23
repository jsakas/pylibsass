import pylibsass

def _setup_tmpdir(tmpdir):
    src = tmpdir.mkdir("app").mkdir("static").mkdir("scss")
    dest = tmpdir.mkdir("app", "static", "css")

    f1 = src.join("test.scss")
    f2 = src.join("test2.scss")

    f1.write(".test { .test-inner { width: 100px; } }")
    f2.write(".test2 { .test2-inner { width: 200px; } }")

    return src, dest

def test_watch_initial_compile(tmpdir):
    src, dest = _setup_tmpdir(tmpdir)

    pylibsass.watch(src.strpath, dest.strpath)

    files = map(lambda f: f.basename, dest.listdir())

    assert set(files) == set(["test.css", "test2.css"])

def test_watch_file_added(tmpdir):
    import time
    src, dest = _setup_tmpdir(tmpdir)

    pylibsass.watch(src.strpath, dest.strpath)

    f = src.join("test3.scss")
    f.write(".test3 { .test3-inner { width: 300px; } }")

    # Give enough time for event to be triggered
    time.sleep(0.05)

    files = map(lambda f: f.basename, dest.listdir())

    assert set(files) == set(["test.css", "test2.css", "test3.css"])
