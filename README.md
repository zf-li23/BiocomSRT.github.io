# Team BiocomSRT Wiki

This repository contains all coding assets to generate our team's wiki (HTML, CSS, JavaScript, TypeScript, Python, Images, photos, icons and fonts, etc).

## Getting started

You should probably only edit the files inside folders `static`, `wiki` and `wiki > pages`.
1. Make the changes on the files you wish:
    * For the menu, change the file [menu.html](wiki/menu.html)
    * For the layout, change the file [layout.html](wiki/layout.html)
    * For the pages, change the corresponding file in the foler [pages](wiki/pages)
2. Review the changes you made
3. Once you are done, save the changes by **committing** them to the *main branch* of the repository 

## About this Template

### Files

The static assets are in the `static` directory. The layout and templates are in the `wiki` directory, and the pages live in the `wiki > pages` directory. Unless you are an experienced and/or adventurous human, you probably shouldn't change other files.

    |__ static/             -> static assets (CSS and JavaScript files only)
    |__ wiki/               -> Main directory for the pages and layouts
        |__ footer.html     -> Footer that will appear in all the pages
        |__ layout.html     -> Main layout of your wiki. All the pages will follow its structure
        |__ menu.html       -> Menu that will appear in all the pages
        |__ pages/          -> Directory for all the pages
            |__ *.html      -> Actual pages of your wiki
    |__ .gitignore          -> Tells GitLab which files/directories should not be uploaded to the repository
    |__ .gitlab-ci.yml      -> Automated flow for building, testing and deploying your website.
    |__ LICENSE             -> License CC-by-4.0, all wikis are required to have this license - DO NOT MODIFY
    |__ README.md           -> File containing the text you are reading right now
    |__ app.py              -> Python code managing your wiki
    |__ dependencies.txt    -> Software dependencies from the Python code

### Technologies

  * [Python](https://www.python.org): Programming language
  * [Flask](https://palletsprojects.com/projects/flask): Python framework
  * [Fronzen-Flask](https://pypi.org/project/Frozen-Flask): Library that builds the wiki to be deployed as a static website
  * [Bootstrap](https://getbootstrap.com/docs/5.3/components): CSS and JS components used

### Building locally (advanced users)

To work locally with this project, follow the steps below:

#### Install
```bash
git clone https://github.com/zf-li23/BiocomSRT.github.io.git
cd BiocomSRT.github.io
python3 -m venv venv
. venv/bin/activate # on Linux, MacOS; or
. venv\Scripts\activate # on Windows
pip install -r dependencies.txt
```

#### Execute
```bash
python app.py
```
