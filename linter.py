from SublimeLinter.lint import ComposerLinter


class Phpcs(ComposerLinter):
    cmd = ('phpcs', '--report=checkstyle', '${args}', '-')
    regex = r'^\s*<error line="(?P<line>\d+)" column="(?P<col>\d+)" severity="(?:(?P<error>error)|(?P<warning>warning))" message="(?P<message>[^"]+)" source="(?P<code>[^"]+)"'  # noqa: E501
    defaults = {
        'selector': 'embedding.php, source.php  - text.blade',
        # we want auto-substitution of the filename,
        # but `cmd` does not support that yet
        '--stdin-path=': '${file}'
    }
