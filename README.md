SublimeLinter-phpcs
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [phpcs](https://github.com/squizlabs/PHP_CodeSniffer).
It will be used with files that have the "PHP", "HTML" and "HTML5" syntax.


## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, ensure that `phpcs` is installed on your system, preferably somewhere in your PATH. To install `phpcs`, follow the instructions on https://github.com/squizlabs/PHP_CodeSniffer#installation. 


## Settings

- SublimeLinter settings: http://sublimelinter.com/en/latest/settings.html
- Linter settings: http://sublimelinter.com/en/latest/linter_settings.html

Use the `"args"` setting to configure the coding standard, if you've not done so via [configuration file](https://github.com/PHPCSStandards/PHP_CodeSniffer/wiki/Annotated-Ruleset). 

```json
{
    "args": [
        "--standard=PEAR", // code standard
    ]
}
```

### Per-project Standards
You can set up your project settings to use a specific standard using the following: 

```json
{
    "settings": {
        "SublimeLinter.linters.phpcs.args": "--standard='${folder}/phpcs.xml'"
    }
}
```
