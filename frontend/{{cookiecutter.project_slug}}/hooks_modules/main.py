import os
import shutil
import git

import hooks_modules.utils as utils


def checkSidebarOption():
    """
    Remove Sidebar from the project if not selected
    """
    # Remove Sidebar from the project if not selected
    pathToRemove = "{% if not cookiecutter.sidebar %} src/components/NavigationDrawer.vue {% endif %}"
    path = pathToRemove.strip()
    if path and os.path.exists(path):
        os.unlink(path)
        utils.removeReferenceFromProject("NavigationDrawer")


def checkNavBarOption():
    """
    Remove Navbar from the project if not selected
    """
    # Remove Navbar from the project if not selected
    pathToRemove = (
        "{% if not cookiecutter.navbar %} src/components/NavBar.vue {% endif %}"
    )
    path = pathToRemove.strip()
    if path and os.path.exists(path):
        os.unlink(path)
        utils.removeReferenceFromProject("NavBar")


def checkBottomNavOption():
    """
    Remove BottomNav from the project if not selected
    """
    # Remove BottomNav from the project if not selected
    pathToRemove = (
        "{% if not cookiecutter.footer %} src/components/BottomNav.vue {% endif %}"
    )
    path = pathToRemove.strip()
    if path and os.path.exists(path):
        os.unlink(path)
        utils.removeReferenceFromProject("BottomNav")


def checkRepositoryNameOption(repo_name):
    """
    Check if repository_name is empty,
    if not init & fill empty git repo
    """
    repo_name = "{{ cookiecutter.repository_name }}"
    if not repo_name:
        return

    shutil.rmtree("hooks_modules")

    g = git.cmd.Git(repo_name)
    g.init()
    g.remote("add", "origin", f"git@github.com:{repo_name}.git")
    g.add(".")
    g.commit("-m", "Commit made by cookiecutter")
    g.branch("-M", "main")

    g.branch("develop")
    g.merge("develop")

    g.branch("uat")
    g.merge("uat")

    g.config("init.defaultBranch", "develop")

    g.push("-u", "origin", "--all")
