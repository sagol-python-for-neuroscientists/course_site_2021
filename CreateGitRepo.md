# How to create your own git repository and synchronize its online and offline parts

This document serves as a reference on the proper way to create a git repo which is located both on your computer and on GitHub. This allows to backup your code "on the cloud", while also simplifying sharing code between developers.

1. Install `git` by completing "Task 2" in `SetupPython.md`.
1. Create a new [GitHub.com](https://github.com) user (or use your existing one).
2. Create a new repository there. Name it. At the bottom of the page choose a Python `.gitignore` file.
The `.gitignore` file specifies the files that are ignored, i.e. _not_ under version control.
4. The page you arrived at is the homepage of your repository (repo). All code you write will
one day be shown there. You can create new files directly from this web interface,
and edit them online as you like.
5. However, a better option is to connect this repo to a folder in your computer, and this is what you'll do next.
This folder can push (_from_ local folder _to_ web) and pull (_from_ web _to_ local folder) data to and from this website,
allowing you to work offline with your own preferred editor and backup and share your code when you wish to.
5. To do so, you can either use the command line or use dedicated software:
    - Basic git command line tool can be installed from [here](https://git-scm.com/downloads).
    - GitHub Desktop.
    - GitKraken.
    - VS Code Git integration (preferred).
    Class 2 includes instructions how to work with the command line interface, and the installation instructions
    can be found in `PythonSetup.md` in the course's website. However, working with the VS Code GUI should be simpler and more intuitive, as I'll show below.
6. The operation we wish to perform is to `clone` the repo to your computer, i.e. creating a copy of the online repo on your computer.
A `clone` operation requires a URL of the respective repo. You can obtain it by clicking the
__Clone or download__ button on the right side of your web repo. Copy the link (the one ending with `.git`). Open VS Code and press `Ctrl[Cmd] + Shift + P` and type `Git: Clone`. Paste the URL to the address bar and choose a folder. Click "Open Repository" to open VS Code inside that folder. This operation "cloned" the online repo and created a copy of it in your computer. You should find inside that folder the `.gitignore` file you created.
8. Now you can create new files inside this folder. When you're happy with the new code you've written, you can commit the changes. Committing means giving a "tag" to a state your code is in. Everytime you do some significant change to your codebase, like adding a function or deleting something, you should commit this change, since it marks a specific milestone in your development process. Git will allow you later to go back to this point in time and review (and possible revert) the changes you've made.
9. To commit, go to the Git symbol on the left bar (fork-looking), highlight the "Changes" row and choose "Stage All Changes". Staging is a required step before committing - you'll commit evert staged changed, but you don't have to stage every change you've made. After staging, you can press the "V" icon on the top to commit the changes to the git tree. VSCode (and git) will request a message describing the changes you've made in your last commit, like "added function x" or "HW is complete".
9. You're now ready to push the changes to the online repo. Click the three dots and select "Push". Enter your credentials and the files should momentarily appear online.
