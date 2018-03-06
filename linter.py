#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Dmitry Tsoy
# Copyright (c) 2013 Dmitry Tsoy
#
# License: MIT
#

from SublimeLinter.lint import Linter, util


class Phpcs(Linter):
    syntax = ('php', 'html', 'html 5')
    cmd = ('phpcs', '--report=emacs', '${args}', '-')
    regex = r'^.*:(?P<line>[0-9]+):(?P<col>[0-9]+): (?:(?P<error>error)|(?P<warning>warning)) - (?P<message>.+)'
    defaults = {
        # we want auto-substitution of the filename, but `cmd` does not support that yet
        '--stdin-path=': '${file}',
        '--standard=': 'PSR2',
    }
    error_stream = util.STREAM_STDOUT
