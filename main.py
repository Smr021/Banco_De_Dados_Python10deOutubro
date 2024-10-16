import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine('sqlite:///meubanco.db') #criando banco SQLite

# CREATE DATABASE meubanco.

# Conecxão com banco de dados.
Session = sessionmaker (bind=db)
session = Session()

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    # Definindo atributos da tabela.
    id = Column('id', Integer,primary_key=True, autoincrement=True)
    nome = Column('nome',String)
    email = Column('email', String)
    senha = Column('senha', String)


    # Definindo atributos da classe.
    def __init__(self,nome:str,email:str,senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

os.system('cls || clear')

# Salvar no bando de dados.
# usuario = Usuario('Marta','marta@gmail.com','123')        
usuario = Usuario(nome='Maria',email='maria@gmail.com',senha='123')
session.add(usuario)
session.commit()

# Mostrando conteúdo do banco de dados.
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f'{usuario.id} - {usuario.nome} - {usuario.email}')






















# Persistir - Banco de Dados
# SGBD
# SQL - Relacionais
# Comandos Criar banco de dados, Tabelas...
# SELECT * FROM CLIENTES
# INSERT, CREATE TABLE, CREATE DATABASE...


# Backend - SQL

# ORM

# INSERT, UPDATE, SELECT *

# pip install sqlalchemy - ferramenta que permite usar o ORM

# bind uma conexão com alguma coisa, no caso com banco de dados