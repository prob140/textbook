# Data 140 Textbook

This textbook was built with [Jupyter Books](https://jupyterbook.org/en/stable/intro.html). This README was written by Shahzar.

## Structure

Only three files/directories need to be edited.
- `_config.yml`: Configuration information about the textbook. Modify this file for things like:
    - changing the logo or favicon;
    - adding or removing launch buttons;
    - changing information about the book.
- `_toc.yml`: Table of contents for the textbook. Modify this file for things like:
    - section and chapter numbering and order;
    - adding or removing sections or chapters.
- `content/`: Content of the textbook. All the notebooks with section and chapter content go here. Modify these files to actually change the content of the sections.

## Maintaining the Textbook
This section details how to maintain the textbook.

### One-time Setup
Follow these steps the first time you set up a computer to modify and maintain the textbook.
1. Create a local copy of this repo by running `git clone https://github.com/prob140/textbook.git` from the command line in whichever folder you want to contain the textbook.
2. Next, you need to install all the required packages. Either of the commands `pip install -r requirements.txt` or `conda install --file requirements.txt` should work. If you have a Windows device, it's preferable to run this in an Anaconda Prompt terminal. This should install the two packages `jupyter-book` and `ghp-import`, which are used for building and deploying the textbook, respectively, and a bunch of other typical packages (e.g. `numpy`, `scipy`, `matplotlib`, etc.) used by the `content/` notebooks.


### Updating the Textbook
These steps detail the process you should go through every time you update the textbook.
1. **Pull:** `cd` into `textbook/`, your local copy of the textbook repo and `git pull origin master` to collect any updates which may have been pushed to the remote copy by other collaborators.
2. **Update:** Make any changes you wish to make. This should (likely) only consist of changes to `_config.yml`, `_toc.yml`, and the files in `content/`.
    - If you added new sections or chapters, update `_toc.yml` as well to reflect your changes.
3. **Build:** `cd` into the directory above `textbook/` (i.e. `cd ..`) and run `jupyter-book build textbook`.
4. **Check:** Open the file `textbook/_build/html/index.html` in your browser to view what the textbook will look like with any changes you've made. Make sure nothing is broken and the changes are as you want them. 
    - See the [Troubleshooting](#troubleshooting) section for any issues you may be having.
    - Take a look at the [Issues](#issues) for problematic parts of the textbook.
5. **Deploy:** `cd` back into `textbook/` (`cd textbook/`) and run `ghp-import -n -p -f _build/html` (the `-n` flag is important, since it adds a `.nojekyll` file which allows GitHub to build the website correctly). This will push the `_build/html` folder to the `gh-pages` branch of the textbook repository, which is configured by GitHub Pages to hold the files for the textbook website. To edit these configurations, from the repository page, go to Settings > Pages.
6. **Push:**  Stage any changes you made (i.e. using `git add [file]`, `git add -u`, `git add .`, etc.), commit your changes with `git commit -m "[description]"` (please include a useful description of any changes you made), and push to the master repository with `git push origin master`.

## Notes
### Troubleshooting
The (Jupyter Book)(https://jupyterbook.org/en/stable/intro.html) website has lots of information about Jupyter Book. Some useful pages are:
- [Anatomy of a Jupyter Book](https://jupyterbook.org/en/stable/start/create.html#anatomy-of-a-jupyter-book)
- [Table of Contents](https://jupyterbook.org/en/stable/structure/configure.html)
- [Configuration Reference](https://jupyterbook.org/en/stable/customize/config.html)
- [References and Cross-References](https://jupyterbook.org/en/stable/content/references.html)
- [Building](https://jupyterbook.org/en/stable/start/build.html)
- [Deploying](https://jupyterbook.org/en/stable/publish/gh-pages.html)

If changes you've made aren't showing up the HTML after building, sometimes deleting `_build` and then building again helps. Jupyter Book will usually only re-build the HTML of notebooks that it thinks have been changed by any edits made, and so this sometimes means that some changes will go unnoticed. Deleting the entire folder and rebuilding forces it to build from scratch, which prevents any old files or code from sticking around.

### Links
Links to the internet should be done as they are usually done in Markdown. However, to cross-link to other pages of the textbook, there is an internal linking system that should be used instead (since it is robust to file structure changes in `/textbook`). This system is described [here](https://jupyterbook.org/en/stable/content/references.html#reference-section-labels).

For example, Section 12.4 Exercise 3 of the [Stat 88 Textbook](stat88.org/textbook) contains a link to Section 12.2. 
1. The flag `(ch12.2)=` was added *before* the primary header of the notebook.
```
(ch12.2)=
## The Distribution of the Estimated Slope ##
```
2. The link to Section 12.2 was changed to `(ch12.2)`.
```
**3.** 
Refer to the regression of active pulse rate on resting pulse rate in [Section 12.2](ch12.2). Here are the estimated values again, along with some additional data.
```

Currently, the Data 140 textbook doesn't use this system for cross-linking, but it should eventually be adapted, as it is more robust to modifications to the file structure.
