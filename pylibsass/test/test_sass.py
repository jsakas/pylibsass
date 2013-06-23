import pytest

from mock import Mock, patch

import textwrap
from pylibsass.sass import compile_str

def test_compile_str():
    src_scss = textwrap.dedent("""
        .test {
            .test-inner {
                width: 100px;
            }
        }
    """)

    css = compile_str(src_scss)

    assert "".join(css.split("\n")) == ".test .test-inner {  width: 100px; }"

