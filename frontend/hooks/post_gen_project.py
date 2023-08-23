import os

# Add root to path, so hooks_modules can be imported from the
# temporary directory created by cookiecutter while generating
# This allows to split the code in multiple files
# https://github.com/cookiecutter/cookiecutter/issues/1593
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
sys.path.insert(0, PROJECT_DIRECTORY)

from hooks_modules import main


if __name__ == "__main__":
    main.checkSidebarOption()
    main.checkNavBarOption()
    main.checkBottomNavOption()
    main.checkRepositoryNameOption("{{ cookiecutter.repository_name }}")
