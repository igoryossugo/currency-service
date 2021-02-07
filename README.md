# currency-service
[![Build Status](https://travis-ci.com/igoryossugo/currency-service.svg?branch=main)](https://travis-ci.com/igoryossugo/currency-service)  
Um serviço para conversões monetárias 

## Instalação (macOS ou Linux)
A aplicação roda em [Python 3.9](https://www.python.org/downloads/release/python-391/) com Django.  
Recomendo a utilização de [pyenv](https://github.com/pyenv/pyenv) para instalação do Python.

### Criando o ambiente
Instalar virtualenv e virtualenvwrapper
```shell
$ python3.9 -m pip install --user virtualenv
$ python3.9 -m pip install virtualenvwrapper
```
Para configurar seu Bash, execute o comando abaixo (recomendo adicionar em seu `~/.bash_profile`)
```shell
$ export WORKON_HOME=~/.virtualenvs
$ source /usr/local/bin/virtualenvwrapper.sh
```
Agora vamos criar o ambiente. Caso esteja usando pyenv:
```shell
$ mkvirtualenv -p ~/.pyenv/versions/3.9.1/bin/python3.9 currency-service
```
Caso contrário:
```shell
$ mkvirtualenv -p /usr/local/bin/python3.9 currency-service
```

Pronto, já temos o ambiente montado para a aplicação. Para mais informações de como criar, deletar, entrar ou sair do seu ambiente, veja a documentação do [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html).  
Agora vamos instalar as dependências do projeto:
```shell
$ make requirements-dev
```

Para rodar as migrations do projeto:
```shell
$ make migrate-dev
```

Para criar o superusuário do admin da aplicação:
```
$ make createsuperuser
```

Para rodar os testes:
```shell
$ make test
```

Para rodar o projeto:
```shell
$ make runserver-dev
```
A aplicação estará disponível no endereço: http://localhost:8000/

Como utilizar:  
https://github.com/igoryossugo/currency-service/wiki