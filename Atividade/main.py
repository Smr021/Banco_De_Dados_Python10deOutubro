import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine('sqlite:///meubancoBD.db')

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
for i in range(2):
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite seu senha: ')

    usuario = Usuario(nome=nome,email=email,senha=senha)
    session.add(usuario)
    session.commit()

# Mostrando conteúdo do banco de dados.
print('\nListando  usuário no banco de dados.')
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f'{usuario.id} - {usuario.nome} - {usuario.email}')

# Deletando um usuário.
usuario = session.query(Usuario).filter_by(email='joao@gmail.com').first()
session.delete(usuario)
session.commit()
print('\nDeletando usuário no banco de dados.')


print('\nListando  usuário no banco de dados.')
lista_usuarios = session.query(Usuario).all()
for usuario in lista_usuarios:
    print(f'{usuario.id} - {usuario.nome} - {usuario.email}')




