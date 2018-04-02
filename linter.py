from SublimeLinter.lint import Linter, util


class Phpcs(Linter):
    cmd = ('phpcs', '--report=emacs', '${args}', '-')
    regex = r'^.*:(?P<line>[0-9]+):(?P<col>[0-9]+): (?:(?P<error>error)|(?P<warning>warning)) - (?P<message>.+)'
    defaults = {
        'selector': 'source.php, text.html.basic',
        # we want auto-substitution of the filename, but `cmd` does not support that yet
        '--stdin-path=': '${file}',
        '--standard=': 'PSR2',
    }
    error_stream = util.STREAM_STDOUT
