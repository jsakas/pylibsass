import pytest

from mock import patch

import textwrap
import pylibsass

def test_compile_str():
    src_scss = textwrap.dedent("""
        .test {
            .test-inner {
                width: 100px;
            }
        }
    """)

    css = pylibsass.compile_str(src_scss)

    assert "".join(css.split("\n")) == ".test .test-inner {  width: 100px; }"
