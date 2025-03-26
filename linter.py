import json
from SublimeLinter.lint import LintMatch, ComposerLinter


class Phpcs(ComposerLinter):
    defaults = {
        'selector': 'embedding.php, source.php  - text.blade',
        # we want auto-substitution of the filename,
        # but `cmd` does not support that yet
        '--stdin-path=': '${file}'
    }
    tab_size = 4

    def find_errors(self, output):
        self.tab_size = self.view.settings().get("tab_size", 4)
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

    def cmd(self):
        if self.view.settings().get("indentation") == 'tabs':
            tab_width = self.view.settings().get("tab_size", 4)
            return ('phpcs', '--report=json', '--tab-width={}'.format(tab_width), '${args}', '-')

        return ('phpcs', '--report=json', '${args}', '-')

    def reposition_match(self, line, col, m, vv):
        line_contents = vv.select_line(line)
        tabs_to_spaces = line_contents[:col].count("\t") * (self.tab_size - 1)
        new_col = max(0, col - tabs_to_spaces)
        return super().reposition_match(line, new_col, m, vv)
