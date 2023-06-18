# Sistema de Gestão de Propostas de Empréstimo Pessoal (SGPEP)

Este é um sistema de gestão de propostas de empréstimo pessoal desenvolvido como parte de um desafio técnico da empresa <a href="https://digitalsys.com.br/"></a>. O objetivo principal do sistema é fornecer uma plataforma robusta e eficiente para gerenciar propostas de empréstimo pessoal.

<br>

<div style="display: flex;">
  <img width="48" height="48" src="https://img.icons8.com/color/48/python--v1.png" alt="python--v1" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/48/external-django-a-high-level-python-web-framework-that-encourages-rapid-development-logo-color-tal-revivo.png" alt="external-django-a-high-level-python-web-framework-that-encourages-rapid-development-logo-color-tal-revivo" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://img.icons8.com/color/48/docker.png" alt="docker" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://img.icons8.com/color/48/javascript--v1.png" alt="javascript--v1" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://upload.wikimedia.org/wikipedia/commons/1/19/Celery_logo.png" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://cdn.freebiesupply.com/logos/large/2x/rabbitmq-logo-png-transparent.png"style="margin-right: 10px;"/>
  
</div>

<br>


1. Clone o projeto em sua máquina.
```bash
   git clone <url do repositorio>
```

2. Crie a virtualenv com o comando (Ambiente Linux).
```bash
   python3 -m venv venv
   source/bin/activate
```

2.1. Crie a virtualenv com o comando (Ambiente Windows).
```bash
   python -m venv venv
   .\venv\Scripts\activate
```

3. Instale os pacotes requeridos.
```bash
   pip install -r requirements.txt
```

4. Migre o projeto.
```bash
   python manege.py migrate
```

4.1. Faça o build do docker-compose.
```bash
   docker-compose up --build
```

5. Start o servidor

```bash
  python manage.py runserver
```
