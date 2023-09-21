## Repositório para as aulas do Instituto Joga Junto

Este repositório contém todo o conteúdo dado das aulas de python do Instituto Joga Junto

## Assuntos abordados:

 - Primeiro contato com python
 - GitHub
 - preparando o ambiente com virtual env
 - Metodos nativos do python ( Print, type, str)
 - Tipos de dados 
 - Operadores: Aritiméticos, de comparação, de atribuição...
 - Collections: Listas, tuplas, sets e dict e seus métodos
 - Estrutura de iteração e repetição
 - Estrutura condicional 
 - Bibliotecas, VirtualEnv e pip
 - Funções

## Comandos em Python:

como criar um ambiente virutal
(EXECUTE O CÓDIGO NO )
```bash
python -m venv nomedoambiente
```

Para o Windows, se tiver problema de policy, executar o comando no powershell como administrador:
```bash
Set-ExecutionPolicy RemoteSigned -Scope Process
```
ou 
```bash
Set-ExecutionPolicy Unrestricted -Force
```

# Para executar o ambiente virtual:

-- Windows:
```bash
nomedoambiente\Scripts\activate
```
Linux/MacOs
```bash
nomedoambiente/bin/activate
```

# Instalar bibliotecas:
Para isso usamos o pip install seguido do nome da lib, não esqueça de pesquisar a biblioteca no google

```bash
pip install nomedabiblioteca
```

# Desinstalar bibliotecas:
Não execute, a não ser que você queira desinstalar as bibliotecas
```bash
pip uninstall nomedabiblioteca
```

# Salvar todos os nomes das dependências do projeto em um arquivo

```bash
pip freeze > requirements.txt
```

Para instalar todas as bibliotecas usadas no projeto, em caso de abrir em outro computador ou mandar pra outra pessoa, deverá ser executado o código abaixo:

```bash
pip install -r requirements.txt
```
Assim, a tag -r antes do nome requirements.txt significa que ele lerá todas as linhas dentro desse arquivo de texto e vai instalar todas as dependências nas versões exatas que estão lá.

