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

[Criando App Contact]
=========================
python manage.py startapp contact
definir as view (index) 
definir a url e app_name
configurar o app no INSTALED_APPS no root
=========================

[Criando Migrations]
=========================
python manage.py makemigrations (Toda vez que alterar algo no models.py, executa o makemigrations)
python manage.py migrate (Toda vez que alterar algo no models.py, executa o migrate)
=========================

[Criando e Configurando Super User]
=========================
python manage.py createsuperuser
python manage.py changepassword USERNAME
=========================

[Django Shell]
=========================
python manage.py shell 
from contact.models import Contact (importar o model)
contato = Contact(**fields) (criar um objeto de forma lazy)
contato.save() (salvar o objeto)
contato = Contact.objects.create(**fields) (criar um objeto de forma explicita)
contato = Contact.objects.get(id=1) (pegar um objeto pelo id ou pk)
contato.field_name1 = 'value' (atualizar um campo)
contato.save() (salvar o objeto)
contato.delete() (deletar o objeto)
=========================