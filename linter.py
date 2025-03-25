import csv
from io import StringIO
from SublimeLinter.lint import LintMatch, ComposerLinter


class Phpcs(ComposerLinter):
    cmd = ('phpcs', '--report=csv', '${args}', '-')
    defaults = {
        'selector': 'embedding.php, source.php  - text.blade',
        # we want auto-substitution of the filename,
        # but `cmd` does not support that yet
        '--stdin-path=': '${file}'
    }

    def find_errors(self, output):
        for match in csv.DictReader(StringIO(output)):
            yield LintMatch(
                line=int(match.get('Line', 1)) - 1,
                col=int(match.get('Column', 1)) - 1,
                error_type=match.get('Type', 'warning'),
                code=match.get('Source', ''),
                message=match.get('Message', ''),
            )
