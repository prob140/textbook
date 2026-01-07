# Data 140 Textbook

[![Jupyter Book (via myst) GitHub Pages Deploy](https://github.com/prob140/textbook/actions/workflows/deploy.yml/badge.svg)](https://github.com/prob140/textbook/actions/workflows/deploy.yml) [![Accessibility Checks](https://github.com/prob140/textbook/actions/workflows/a11y.yml/badge.svg)](https://github.com/prob140/textbook/actions/workflows/a11y.yml)

This textbook was built with [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). 

## Structure

Only two things need to be edited.
- `myst.yml`: Configuration information about the textbook. Modify this file for things like:
    - changing the logo or favicon;
    - adding or removing launch buttons;
    - changing information about the book.
    - table of contents (section, chapter numbering and order)
- `content/`: Content of the textbook. All the notebooks with section and chapter content go here. Modify these files to change the content of the sections.

## Maintaining the Textbook
This section details how to maintain the textbook.

### One-time Setup
Follow these steps the first time you set up a computer to modify and maintain the textbook.
1. Create a local copy of this repo by running `git clone https://github.com/prob140/textbook.git` from the command line in whichever folder you want to contain the textbook.
2. Next, you need to install all the required packages. Either of the commands `pip install -r requirements.txt` or `conda install --file requirements.txt` should work. If you have a Windows device, it's preferable to run this in an Anaconda Prompt terminal. This should install the two packages `jupyter-book` and `ghp-import`, which are used for building and deploying the textbook, respectively, and a bunch of other typical packages (e.g. `numpy`, `scipy`, `matplotlib`, etc.) used by the `content/` notebooks. If you use pip to install the packages, I recommend using a python virtual environment:
```
python3 -m venv venv # create virtual environment
source venv/bin/activate # activate the virtual environment
pip install -r requirements.txt # as above
```
If you use a virutal environment, make sure to activate it before updating the textbook by first running `source venv/bin/activate` at the root of this repo. You can deactivate the environment with `deactivate`.

### Updating the Textbook
These steps detail the process you should go through every time you update the textbook.
1. **Pull:** `cd` into `textbook/`, your local copy of the textbook repo and `git pull origin master` to collect any updates which may have been pushed to the remote copy by other collaborators.
2. **Update:** Make any changes you wish to make. This should (likely) only consist of changes to `_myst.yml` and the files in `content/`.
    - If you added new sections or chapters, update `myst.yml` as well to reflect your changes.
3. **Build and Check:** `cd` into the directory above `textbook/` (i.e. `cd ..`) and run `jupyter book start` to build the book and serve it on localhost. View what the textbook will look like with any changes you've made. Make sure nothing is broken and the changes are as you want them. 
    - See the [Troubleshooting](#troubleshooting) section for any issues you may be having.
    - Take a look at the [Issues](#issues) for problematic parts of the textbook.
6. **Push:**  Stage any changes you made (i.e. using `git add [file]`, `git add -u`, `git add .`, etc.), commit your changes with `git commit -m "[description]"` (please include a useful description of any changes you made), and push to the master repository with `git push origin master`. Deployment will happen automatically via GitHub Actions.

### Deployment
The textbook is hosted on GitHub Pages and deployed automatically everytime you push to the master branch via [this workflow](https://github.com/prob140/textbook/actions/workflows/deploy.yml).

## Notes
The [Jupyter Book](https://jupyterbook.org/stable/) website has lots of information about Jupyter Book. This textbook has been upgraded to Jupyter Book v2 built on [MyST](https://mystmd.org/).

If changes you've made aren't showing up the HTML after building, sometimes deleting `_build` and then building again helps. You can also run `jupyter book clean`.

Some cells are hidden with tags like `remove-input` or `remove-cell`. 

### Links
Links to the internet should be done as they are usually done in Markdown. However, to cross-link to other pages of the textbook, there is an internal linking system that should be used instead (since it is robust to file structure changes). This system is described [here](https://mystmd.org/guide/cross-references#targeting-headers). 

For example, Section 12.4 Exercise 3 of the [Stat 88 Textbook](https://github.com/stat88/textbook) contains a link to Section 12.2. 
1. The flag `(ch12.2)=` was added *before* the primary header of the notebook.
```
(ch12.2)=
## The Distribution of the Estimated Slope ##
```
2. The link referencing Section 12.2 is created like so:
```
**3.** 
Refer to the regression of active pulse rate on resting pulse rate in [Section 12.2](ch12.2). Here are the estimated values again, along with some additional data.
```
