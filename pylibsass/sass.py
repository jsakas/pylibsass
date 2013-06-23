from ctypes import *

class SassOptions(Structure):
    _fields_ = [
        ("output_style", c_int),
        ("source_comments", c_int),
        ("include_paths", c_char_p),
        ("image_path", c_char_p),
    ]

class SassContext(Structure):
    _fields_ = [
        ("source_string", c_char_p),
        ("output_string", c_char_p),
        ("sass_options", SassOptions),
        ("error_status", c_int),
        ("error_message", c_char_p),
    ]

class SassFileContext(Structure):
    _fields_ = [
        ("input_path", c_char_p),
        ("output_string", c_char_p),
        ("sass_options", SassOptions),
        ("error_status", c_int),
        ("error_message", c_char_p),
    ]

class SassFolderContext(Structure):
    _fields_ = [
        ("search_path", c_char_p),
        ("output_path", c_char_p),
        ("sass_options", SassOptions),
        ("error_status", c_int),
        ("error_message", c_char_p),
    ]

SASS_CLIB = cdll.LoadLibrary('sass.so')
SASS_CLIB.sass_new_context.restype = POINTER(SassContext)
SASS_CLIB.sass_new_file_context.restype = POINTER(SassFileContext)
SASS_CLIB.sass_new_folder_context.restype = POINTER(SassFolderContext)

SASS_CLIB.sass_compile.restype = c_int
SASS_CLIB.sass_compile.argtypes = [POINTER(SassContext)]

SASS_CLIB.sass_compile_file.restype = c_int
SASS_CLIB.sass_compile_file.argtypes = [POINTER(SassFileContext)]

SASS_CLIB.sass_compile_folder.restype = c_int
SASS_CLIB.sass_compile_folder.argtypes = [POINTER(SassFolderContext)]

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
