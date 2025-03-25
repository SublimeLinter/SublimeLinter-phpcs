import json
from SublimeLinter.lint import LintMatch, ComposerLinter


class Phpcs(ComposerLinter):
    cmd = ('phpcs', '--report=json', '${args}', '-')
    defaults = {
        'selector': 'embedding.php, source.php  - text.blade',
        # we want auto-substitution of the filename,
        # but `cmd` does not support that yet
        '--stdin-path=': '${file}'
    }

    def find_errors(self, output):
        data = json.loads(output)
        for file_path, file_data in data["files"].items():
            for error in file_data['messages']:
                yield LintMatch(
                    filename=file_path,
                    line=error['line'] - 1,
                    col=error['column'] - 1,
                    error_type=error['type'].lower(),
                    code=error['source'],
                    message=error['message'],
                )
