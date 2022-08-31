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

### Upload to google drive

The workflow automatically uploads file to a google drive folder to configure set 
`FOLDER_ID` and `CREDENTIALS_BASE64` in repo secrets, The workflow uploads multiple 
flavours of resumes based on branch names eg. `main: resume.pdf`, `new: resume-new.pdf`.

`CREDENTIALS_BASE64` can be obtained by running 

```shell
base64 -iw0 credentials.json > credentials.base64
```

Script usage:
```shell
pip install -r scripts/requirements.txt
python scripts/upload.py [folder_id] [credentials_path] build/resume.pdf
```

If there is a file with same name in the selected folder the script will upload a 
[new version](https://support.google.com/drive/answer/2409045) of the file.

### Todo

- Make replacement of class files easier
