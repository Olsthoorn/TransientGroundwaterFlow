# How to generate sphinx documentation from LyX

Theo Olsthoorn, 2022-05-03


Set: document>settings>language>encoding --> utf8


## Intro

This markdown file explains how to generate sphinx documentation from the **LyX** app. It's most useful to work with **markdown** files in **VSCODE**, because it allows linting making sure errors are found early and offering explanations and solutions.

The **markdown** file can then immediately rendered to **HTML** by using the command <u>**^-cmd-P**</u> <u>**Markdown All in one: Print current document to HTML**</u> for easy visualization.

## Pictures of the LyX document

A **Lyx** document with a lot of pictures can feel crowdy if both are stored in the same directory. To store pictures an another directory while sitll being found by **LyX**, change inside the LyX file all instances with **`filename `** with something like **`filename ./pictures/`** to prepend the relative path to the local file name already stored in **LyX** like for istance **`filname thispic.png`**, which then becomes **`filename ./pictures/thispic.png`** and likewise for all other picture files.

## Inline formulas withou a space in front

Inline formulaes may pop-up in `LyX` without a space between the previous word and the formula for unknown reasons. This, however, can be solved by loading the `.lyx' file in the VScode editor and replace '[A-Za-z.,;;]\n\\begin_inset Formula` by ' \n\begin_inset Formula` Thus inserting the space before the formula. When the `.lyx` file is reloaded, the problem is solved.

## First things first

Latex has to be **`utf8`** encoded.

To do this from within the **LyX** app, choose

    `document>settings>language>encoding>other`

Which sets

    ``\usepackage[T1]{fontenc}``
    ``\usepackage[utf8]{inputenc}``

In the Latex output immediately after

    `\documentclass[english]{scrreprt}`

Then choose ``Unicode (utf8)`` from the dropdown menu under ``encoding>other``

Add special characters to the preamble (I'm not sure if it is really necessary, though).

From

    ``document>settings>Preamble``

## Generating `docs` and lower directories by running `sphinx-quickstart`

To generate the HTML documentation by `sphinx` it needs to be installed first (if not already done).

First create a separate sphinx environment to be sure it does not conflict with anything else. On the other hand, when `sphinx` is run, it will import the python files and, therefore, executed it, so it must be able to find imports. This may not be possible in the separate `sphinx` environment if the modules and packages can't be found there. In this case, install `sphinx` in the working environment.

Then activate the **`sphinx`** venv (if not, then run

Installing and activating `sphinx` can be done as follows:

```sh
conda install sphinx  # this first
conda activate sphinx
```
## Making a `docs` directory and running `sphinx-quickstart` from there

If there is no **`docs`** folder then first make it an change directory to it,

```sh
mkdir docs
chdir docs
```

Then run

```sh
sphinx-quickstart
```

Then change directory to the created **`docs/source/`** directory and edit the `conf.py` file that `sphinx-quistart` put there:

I.e. in the top of conf.py remove the `#` before import os and import sys and the next line.
Then change the `sys.path.insert` line to include the directory with the *source data* (i.e. the *.rst files) relative to the **`docs/source/`** folder, i.e. to **`../../`** instead of **`'.'`**, so:

```py
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
```

You may also wish to change the **`theme`** from the default **`alabaster`** to **`spinx_rtd_theme`**:

```py
import sphinx_rtd_theme
extensions += ['sphinx_rdt_theme']
html_theme = 'spinx_rtd_theme' # alabaster'
```

## Generate the `.tex` file

From within **`LyX`** do **`file>export`** to <u>**LaTex (pdflatex)**</u>, which is the most used.

This file will thebn resied next to the `.lyx` file in the directory above `docs/`.

Then on the command line from the `docs/source/` directory use **`pandoc`** app to convert the obtained **`.tex`** file to required **`.rst`** file.

However, assuming the original `.tex` file is above the `docs` directory and we are in `docs/source/` diretory, run

```bash
pandoc -s --from=latex --to=rst -o TransientGroundwater.rst ../../TransientGroundwater.tex
```

This will place the resulting `.rst` file in the `docs/source` directory.

Look in the **`docs>source/`** directory for the file **`index.rst`**.

Then add **`TransientGroundwater`** on a line below the **`..toctree:`**.

Then make the documentation from within the `docs` directory:

```sh
make clean
make html
```

Finally:

Change directory to **`docs/build`** click **index.html**

## Problem with the rst file causing errors when making HTLM

Sphinx reports errors with the `.rst` file when converting to `HTML`. It says there is an error in the option block of each figure. As it turns out it it sthe `:alt:` directive. The `rst` documentation says that this should be a simple text used to show for instance on screen or on sheets instead of long captions. After trying out, it turns out that the text after the `:alt:` label may only be a single line. As pandoc as copied the entire caption of each figure to the :alt: label, which are mostly more than one line in the `.rst' file, it yields errors.

The simple solution is to run a python file called `cleanRst.py` to replace the long multiline text after `:alt:` labels by a short one. A solution for this is to use the pictures file name without the extension for this purpose.
