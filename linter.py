#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dmitry Tsoy
# Copyright (c) 2013 Dmitry Tsoy
#
# License: MIT
#

"""This module exports the Phpcs plugin class."""

from SublimeLinter.lint import Linter


class Phpcs(Linter):

    """Provides an interface to phpcs."""

    syntax = ('php', 'html', 'html 5')
    regex = (
        r'.*line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?:(?P<error>error)|(?P<warning>warning))" '
        r'message="(?P<message>.*)" source'
    )
    executable = 'phpcs'
    cmd = 'phpcs --report=checkstyle'
    defaults = {
        '--standard=': 'PSR2',
    }
    inline_overrides = ('standard')
    tempfile_suffix = 'php'
