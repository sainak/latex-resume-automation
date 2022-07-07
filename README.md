# LaTeX Resume

This repo contains configs and workflow to automatically generate pdfs from a LaTeX resume.

### Features

- compile resume to pdf
- support for external tex classes
- uses LuaLatex as compiler
- auto deploys to github pages

### Requirements

##### Arch Linux

```shell
pacman -S texlive-bin biber texlive-bibtexextra texlive-fontsextra texlive-latexextra
```

### Usage

```shell
make build preview
```

### Todo

- Ability to upload generated resume to online storage accounts
- Make replacement of class files easier
