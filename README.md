SublimeLinter-phpcs
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-phpcs.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-phpcs)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org/) provides an interface to [phpcs](http://pear.php.net/package/PHP_CodeSniffer/). It will be used with files that have the “PHP”, “HTML” and “HTML5” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `phpcs` is installed on your system, preferably somewhere in your PATH. To install `phpcs`, follow the instructions on https://github.com/squizlabs/PHP_CodeSniffer#installation. 

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

### Project Specific Executable
It is possible to specify the `phpcs` executable that should be used to lint your code on a per-project level.

**Example:**
```json
{
    "SublimeLinter": {
        "linters": {
            "phpcs": {
                "cmd": "${folder}/vendor/bin/phpcs"
            }
        }
    }
}
```

### Per-project Standards
You can set up your project settings to use a specific standard using the following: 

```json
{
    "SublimeLinter": {
        "linters": {
            "phpcs": {
                "standard": "${folder}/phpcs.xml"
            }
        }
    }
}
```
