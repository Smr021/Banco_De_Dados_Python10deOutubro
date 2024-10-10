import os
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine('sqlite:///meubanco.db') #criando banco SQLite

# CREATE DATABASE meubanco.

# Conecxão com banco de dados.
Session = sessionmaker (bin=db)
Session = Session()

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

Base.metadata.create_all(bind=db)
        























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