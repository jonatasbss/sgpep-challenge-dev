# Sistema de Gestão de Propostas de Empréstimo Pessoal (SGPEP)

#### Este é um sistema de gestão de propostas de empréstimo pessoal desenvolvido como parte de um desafio técnico da empresa <a href="https://digitalsys.com.br/">Digitalsys Tecnologia</a>. O objetivo principal do sistema é fornecer uma plataforma robusta e eficiente para gerenciar propostas de empréstimo pessoal.

<br>

<div style="display: flex;justify-content: center;">
  <img width="48" height="48" src="https://img.icons8.com/color/48/python--v1.png" alt="python--v1" style="margin-right: 10px;"/>
  <img width="55" height="55" src="https://img.icons8.com/color/48/django.png" alt="django" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://img.icons8.com/color/48/docker.png" alt="docker" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://img.icons8.com/color/48/javascript--v1.png" alt="javascript--v1" style="margin-right: 10px;"/>
  <img width="48" height="48" src="https://upload.wikimedia.org/wikipedia/commons/1/19/Celery_logo.png" style="margin-right: 10px;"/>
  <img width="45" height="45" src="https://cdn.freebiesupply.com/logos/large/2x/rabbitmq-logo-png-transparent.png" style="margin-right: 10px;"/>

</div>

<br>

<div style="display: flex; align-items: center;">
  <span style="margin-right: 10px;font-weight: bold; font-size: 25px">Tecnologias Utilizadas</span>
  <img width="48" height="48" src="https://img.icons8.com/stickers/48/technology.png" alt="technology"/>
</div>

<hr>

<p style="font-weight: bold">O sistema foi construído utilizando a seguinte stack de tecnologias:</p>

- <b>Django</b>: Um framework web de alto nível escrito em Python que permite o desenvolvimento rápido e seguro de aplicações web.
- <b>Django Rest Framework</b>: Uma poderosa biblioteca que complementa o Django, fornecendo recursos para facilitar a criação de APIs RESTful.
- <b>Django Celery</b>: Uma ferramenta assíncrona de tarefas distribuídas, que permite a execução de tarefas em segundo plano de forma eficiente e escalável.
- <b>RabbitMQ</b>: Um sistema de mensagens assíncronas que funciona como intermediário entre os diferentes componentes do sistema, garantindo a comunicação confiável e eficiente entre eles.
- <b>Docker</b>: Uma plataforma de virtualização que permite empacotar o sistema e suas dependências em contêineres isolados, proporcionando portabilidade e facilitando o processo de implantação em diferentes ambientes.

<br>


<div style="display: flex; align-items: center;">
  <span style="margin-right: 10px;font-weight: bold; font-size: 25px">Funcionalidades Principais</span>
  <img width="48" height="48" src="https://img.icons8.com/color/48/gears.png" alt="gears"/>
</div>

<hr>

<p style="font-weight: bold">O sistema de gestão de propostas de empréstimo pessoal oferece as seguintes funcionalidades principais:</p>

- <b>Cadastro de Propostas</b>: Os usuários podem cadastrar novas propostas de empréstimo pessoal, fornecendo informações detalhadas sobre o valor do empréstimo, prazo, taxa de juros, entre outros.
- <b>Listagem de Propostas</b>: Os usuários podem visualizar uma lista de todas as propostas de empréstimo cadastradas no sistema, com a possibilidade de aplicar filtros e ordenar os resultados.
- <b>Execução Assíncrona de Tarefas</b>: O sistema utiliza o Django Celery em conjunto com o RabbitMQ para executar tarefas em segundo plano, como processamento de propostas, envio de notificações, entre outras, de forma escalável e eficiente.
- <b>API RESTful</b>: O sistema oferece uma API RESTful para integração com outros sistemas, permitindo a criação, leitura, atualização e exclusão de propostas de empréstimo por meio de endpoints específicos.

<br>

<div style="display: flex; align-items: center;">
  <span style="margin-right: 10px;font-weight: bold; font-size: 25px">Executando o Sistema</span>
  <img width="48" height="48" src="https://img.icons8.com/external-microdots-premium-microdot-graphic/48/external-gears-communication-multimedia-vol1-microdots-premium-microdot-graphic.png" alt="external-gears-communication-multimedia-vol1-microdots-premium-microdot-graphic"/>
</div>

<hr>

1 - Clone o projeto em sua máquina.

```bash
git clone <url do repositorio>
```

2 - Crie a virtualenv com o comando (Ambiente Linux).

```bash
python3 -m venv venv
source/bin/activate
```

<div style="display: flex; align-items: center;">
  <span style="margin-right: 10px;font-weight: bold; font-size: 25px">Ambiente Windows</span>
  <img width="40" height="40" src="https://img.icons8.com/color/48/windows-10.png" alt="windows-10"/>
</div>

<hr>

<p style="font-weight: bold">Para um configuração no ambiente windowns é necessário fazer um configuração via terminal PowerShell, para não ter problemas com a criação e ativação da sua venv.</p>

2.1 - Pesquise na barra de pesquisa do menu iniciar por 'Windows PowerShell' e o execute como administrador. Quando ele
abrir execute o seguinte comando.

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

2.2 - Crie a virtualenv com o comando (Ambiente Windows).

```bash
python -m venv venv
.\venv\Scripts\activate
```

3 - Instale os pacotes requeridos.

```bash
pip install -r requirements.txt
```

4 - Migre o projeto.

```bash
python manege.py migrate
```

4.1 - Faça o build do docker-compose.

```bash
docker-compose up --build
```

5 - Start o servidor

```bash
python manage.py runserver
```

6 - Rabbitmq: Caso o celery não consiga se conectar com o rabbitmq, rode esse camando no seu terminal, para pegar o ip onde o rabbitmq está rodando e alterar no .env
```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' rabbitmq
```