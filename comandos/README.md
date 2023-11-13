[Iniciar Projeto Django]
========================
python -m venv venv
venv\Scripts\activate.bat
pip install django
django-admin startproject project .
=========================

[Configurar o GIT]
=========================
git config --global user.name 'seu nome'
git config --global user.email 'seu email@gmail.com'
git config --global init.defaultBranch main
configurar o .gitignore
git init
git add .
git commit -m 'commit inicial'
git log --oneline (Ver o commit)
git remote add origin https://github.com/username/project.git (HTTPS)
git push --set-upstream origin main
=========================