from SublimeLinter.lint import ComposerLinter


class Phpcs(ComposerLinter):
    cmd = ('phpcs', '--report=emacs', '${args}', '-')
    regex = r'^.*:(?P<line>[0-9]+):(?P<col>[0-9]+): (?:(?P<error>error)|(?P<warning>warning)) - (?P<message>.+)'
    composer_name = 'phpcs'
    defaults = {
        'selector': 'source.php - text.blade, text.html.basic',
        # we want auto-substitution of the filename, but `cmd` does not support that yet
        '--stdin-path=': '${file}'
    }
