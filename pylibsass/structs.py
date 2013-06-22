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
