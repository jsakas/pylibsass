import fnmatch
import os

from ctypes import *

from pylibsass import structs
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SASS_CLIB = cdll.LoadLibrary('sass.so')
SASS_CLIB.sass_new_context.restype = POINTER(structs.SassContext)
SASS_CLIB.sass_new_file_context.restype = POINTER(structs.SassFileContext)
SASS_CLIB.sass_new_folder_context.restype = POINTER(structs.SassFolderContext)

SASS_CLIB.sass_compile.restype = c_int
SASS_CLIB.sass_compile.argtypes = [POINTER(structs.SassContext)]

SASS_CLIB.sass_compile_file.restype = c_int
SASS_CLIB.sass_compile_file.argtypes = [POINTER(structs.SassFileContext)]

SASS_CLIB.sass_compile_folder.restype = c_int
SASS_CLIB.sass_compile_folder.argtypes = [POINTER(structs.SassFolderContext)]

def _compile(ctx):
    return SASS_CLIB.sass_compile(ctx)

def _compile_file(ctx):
    return SASS_CLIB.sass_compile_file(ctx)

def _compile_folder(ctx):
    return SASS_CLIB.sass_compile_folder(ctx)

def compile_str(contents):
    """Compiles a SASS string

    :param str contents: The SASS contents to compile
    :returns: The compiled CSS

    """
    ctx = SASS_CLIB.sass_new_context()
    ctx.contents.source_string = c_char_p(contents)

    _compile(ctx)

    return ctx.contents.output_string

def watch(source_path, dest_path):
    # Setup Watchdog
    handler = Events(source_path, dest_path)
    observer = Observer(timeout=5000)
    observer.schedule(handler, path=source_path, recursive=True)
    observer.start()

class Events(FileSystemEventHandler):
    """Handler for all filesystem events."""

    def __init__(self, source_path, dest_path):
        super(Events, self).__init__()

        self._source_path = source_path
        self._dest_path = dest_path

    def get_scss_files(self, skip_partials=True, with_source_path=False):
        """Gets all SCSS files in the source directory.

        :param bool skip_partials: If True, partials will be ignored. Otherwise,
                                   all SCSS files, including ones that begin
                                   with '_' will be returned.
        :param boom with_source_path: If true, the `source_path` will be added
                                      to all of the paths. Otherwise, it will
                                      be stripped.
        :returns: A list of the SCSS files in the source directory

        """
        scss_files = []

        for root, dirs, files in os.walk(self._source_path):
            for filename in fnmatch.filter(files, "*.scss"):
                if filename.startswith("_") and skip_partials:
                    continue

                full_path = os.path.join(root, filename)
                if not with_source_path:
                    full_path = full_path.split(self._source_path)[1]

                scss_files.append(full_path)

        return scss_files

    def on_any_event(self, event):
        if not os.path.exists(self._dest_path):
            os.makedirs(self._dest_path)

        for scss_file in self.get_scss_files():
            # Read in the source SCSS file contents
            contents = ""
            with open(os.path.join(self._source_path, scss_file)) as open_file:
                contents = open_file.read()

            # Write out the CSS file
            css_filename = os.path.splitext(scss_file)[0] + ".css"

            with open(os.path.join(self._dest_path, css_filename), 'w') as css_file:
                css_file.write(compile_str(contents))
