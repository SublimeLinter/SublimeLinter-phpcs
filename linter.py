#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dmitry Tsoy
# Copyright (c) 2013 Dmitry Tsoy
#
# License: MIT
#

from SublimeLinter.lint import Linter


class Phpcs(Linter):
    syntax = ('php', 'html', 'html 5')
    cmd = ('phpcs', '--report=checkstyle', '${args}', '-')
    regex = (
        r'.*line="(?P<line>\d+)" '
        r'column="(?P<col>\d+)" '
        r'severity="(?:(?P<error>error)|(?P<warning>warning))" '
        r'message="(?P<message>.*)" source'
    )
    defaults = {
        # we want auto-substitution of the filename, but `cmd` does not support that yet
        '--stdin-path=': '${file}',
        '--standard=': 'PSR2',
    }
