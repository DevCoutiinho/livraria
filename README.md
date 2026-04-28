# Livraria Python

Este projeto é uma aplicação web para o gerenciamento de uma livraria, desenvolvida em Python. O objetivo deste documento é fornecer uma visão geral sobre o projeto, a arquitetura adotada, as ferramentas utilizadas e as convenções que devem ser seguidas durante o seu desenvolvimento.

## 🚀 Tecnologias Utilizadas (Stack)

A aplicação utiliza as seguintes tecnologias:

- **Python**: Linguagem de programação principal trabalhando no back-end.
- **Flask**: Micro-framework web utilizado para construir a API e gerenciar as rotas.
- **HTML5 & CSS3**: Para estruturação semântica e customização de estilos da interface.
- **JavaScript**: Para tornar o front-end dinâmico e interativo no lado do cliente.
- **Bootstrap**: Framework CSS utilizado para agilizar o desenvolvimento responsivo e criar componentes visuais modernos.

## 🐍 Ambiente Virtual (venv)

Para garantir que as dependências do projeto não entrem em conflito com outras aplicações Python na sua máquina, é **altamente recomendável e necessário** o uso de um ambiente virtual (`venv`). O ambiente virtual isola os pacotes instalados para o projeto (como `flask` e `flask-sqlalchemy`), garantindo que as versões fiquem restritas a esta aplicação.

**Como criar, ativar e instalar as dependências de ambiente:**

1. **Criação do ambiente** (execute apenas uma vez, na raiz do diretório do projeto):
   ```bash
   python -m venv .venv
   ```

2. **Ativação do ambiente** (execute sempre que abrir o terminal para trabalhar no projeto):
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - No LinuX/MacOS:
     ```bash
     source .venv/bin/activate
     ```

3. **Instalação de pacotes**:
   Com o ambiente ativado (você verá `(.venv)` no início da linha do terminal), você deve instalar os pacotes do projeto usando o `pip`:
   ```bash
   pip install flask flask-sqlalchemy
   ```

## 🌿 Versionamento de Código com Git Flow

Neste projeto, é **obrigatório o uso do Git Flow** como estratégia de versionamento de código. Isso garante um workflow organizado, permitindo que o desenvolvimento de novas features, correções de bugs e lançamentos de novas versões ocorram de forma padronizada sem comprometer o código em produção.

**Ramos principais (branches):**
- `main` (ou `master`): Contém o código de produção, sempre estável.
- `develop`: Contém o código pré-produção. É a base onde todas as novas funcionalidades são integradas para testes.

**Ramos de apoio:**
- `feature/*`: Usados para desenvolver novas funcionalidades (ex: `feature/cadastro-livros`). Nascem a partir do `develop` e são mesclados de volta no `develop`.
- `bugfix/*`: Usados para correções de bugs durante o desenvolvimento.
- `hotfix/*`: Usados para correções urgentes aplicadas diretamente em produção (nascem da `main` e são mesclados tanto na `main` quanto no `develop`).
- `release/*`: Usados para as preparações finais de lançamentos (nascem no `develop` e são mesclados na `main` e também no `develop`).

**Exemplo básico de uso:**
```bash
# Iniciando uma nova feature de cadastro
git flow feature start cadastro-usuario

# ... desenvolvimento do código associado ...

# Finalizando a feature (juntará no develop automaticamente e deletará o ramo feature local)
git flow feature finish cadastro-usuario
```

## 🏗️ Padrão de Arquitetura: MVC (Model-View-Controller)

O projeto deve estritamente seguir o padrão de arquitetura **MVC** para garantir uma forte separação de responsabilidades. Isso significa que o código deve ser organizado nas seguintes camadas:

1. **Model (M - Modelo)**: Responsável por gerenciar os dados, regras de negócio e o estado lógico do aplicativo (geralmente ligado ao banco de dados).
2. **View (V - Visão)**: Responsável pela interface gráfica onde o usuário interage, ou seja, as telas, botões, exibições em HTML e Bootstrap.
3. **Controller (C - Controlador)**: Intermediário vivo entre o Model e a View. Recebe as requisições das rotas do Flask, processa os dados solicitados pelo Model e decide qual View renderizar para o cliente.

### Estrutura de Pastas MVC com Flask

Para aplicar o MVC em nossa estrutura com o Flask, os arquivos e lógicas devem ser distribuídos da seguinte maneira, mantendo o código mais limpo:

```text
livraria-python/
│
├── app.py                      # Arquivo de inicialização, configuração e roteamento principal
├── controllers/
│   └── livro_controller.py     # Lógicas de processamento e resposta envolvendo livros
├── models/
│   └── livro_model.py          # Entidades, acesso e regras de persistência referentes a livros
├── templates/                  # Equivale à camada VIEW no Flask
│   └── livros.html             # Interface com HTML e Bootstrap para os usuários
└── static/                     # Arquivos estáticos
    ├── css/
    └── js/
```

### Exemplo Base de Implementação

**1. O Model (`models/livro_model.py`)** - Regras e processamento de dados.
```python
# Simula a estrutura de banco de dados
banco_de_livros = []

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    @staticmethod
    def salvar(livro):
        banco_de_livros.append(livro)
        return True

    @staticmethod
    def listar_todos():
        return banco_de_livros
```

**2. O Controller (`controllers/livro_controller.py`)** - Orquestra a operação.
```python
from flask import render_template, request, redirect, url_for
from models.livro_model import Livro

def listar_livros():
    livros = Livro.listar_todos()
    # Envia os dados manipulados do model para serem exibidos na "view" associada
    return render_template('livros.html', livros=livros)

def adicionar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        
        # Controlador utiliza a estrutura Model
        novo_livro = Livro(titulo, autor)
        Livro.salvar(novo_livro)
        
        return redirect(url_for('listar_livros'))
```

**3. A View (`templates/livros.html`)** - Onde incluímos os layouts.
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Livraria Python</title>
    <!-- Incluindo Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="container mt-4">
    <h1 class="text-primary mb-3">Livraria - Acervo</h1>
    
    <ul class="list-group mb-4">
        {% for livro in livros %}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                {{ livro.titulo }} 
                <span class="badge bg-secondary rounded-pill">{{ livro.autor }}</span>
            </li>
        {% endfor %}
    </ul>

    <div class="card card-body">
        <h3>Adicionar Novo Livro</h3>
        <form action="/adicionar" method="POST">
            <div class="mb-3">
                <label class="form-label">Título</label>
                <input type="text" name="titulo" class="form-control" required>
            </div>
            <div class="mb-3">
                <label class="form-label">Autor</label>
                <input type="text" name="autor" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-success">Salvar no Acervo</button>
        </form>
    </div>
</body>
</html>
```

## 🗄️ Gerenciamento do Banco de Dados (Flask-Migrate)

Como usamos o SQLAlchemy para criar nossa camada de Modelos, as alterações na estrutura do banco de dados (tabelas, colunas, etc.) precisam ser rastreadas de forma versionada. Para isso, utilizamos a ferramenta **Flask-Migrate**. 

### Comandos Principais

Sempre com seu ambiente virtual (`venv`) **ativado** e posicionado na raiz do projeto (onde está o seu arquivo de inicialização, que em nosso caso é o `run.py`), utilize os seguintes comandos do terminal:

- `flask db init`: Prepara o banco de dados e cria a pasta `migrations/`. **Atenção:** Só deve ser executado **uma única vez** no nascimento do projeto. Se a pasta `migrations/` já existe, nunca rode esse comando novamente!
- `flask db migrate -m "Sua mensagem"`: Gera um novo script de migração. O Flask detecta automaticamente as alterações feitas nos arquivos e classes dentro de `models/` em relação ao último estado do banco. Lembre-se sempre de ser claro na mensagem (ex: `"Adicionando tabela de pedidos"` ou `"Nova coluna estoque em livros"`).
- `flask db upgrade`: Aplica de fato as alterações geradas pelo comando `migrate` no seu banco de dados local (SQLite).

### ⚠️ Práticas e O que EVITAR:
1. **Nunca altere as tabelas do banco manualmente por fora:** Sempre modifique o esquema manipulando os arquivos da pasta `models/` no código Python e deixando que a dupla `migrate` + `upgrade` faça o trabalho no banco.
2. **Nunca apague a pasta `migrations/` e os arquivos dentro de `migrations/versions/`:** Eles mantêm o registro sequencial de como o banco evoluiu. Remover isso causa confusão e erro nas próximas atualizações de ambiente.
3. **Errou antes do Upgrade?** Se você rodou o `flask db migrate`, viu o arquivo que foi criado e percebeu que errou em algo no código, não mexa no banco. Bastará deletar o arquivo python com a respectiva revisão gerado dentro de `migrations/versions/`, consertar seu código em `models/` e rodar `flask db migrate` mais uma vez.

Adotando essas definições, a **Livraria Python** manterá um código escalável, limpo e adequado às demandas avançadas da engenharia de software para projetos web.
