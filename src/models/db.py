from peewee import *

mysql_db = MySQLDatabase('contratosv1',user='ADMCOIMBRA',password='123456SETE',host='localhost')

class BaseModel(Model):
    class Meta:
        database = mysql_db

class Contratante(BaseModel):
    razao_social = CharField(90)
    endereco = CharField(200)
    cnpj = BigIntegerField(14)
    telefone = CharField(10)
    
    class Meta:
        db_table = 'contratante'

class Contratado(BaseModel):
    razao_social = CharField(90)
    endereco = CharField(200)
    cnpj = BigIntegerField(14)
    telefone = CharField(10)
    
    class Meta:
        db_table = 'contratado'

class TipoContrato(BaseModel):
    tipo = CharField(20)
    objeto = CharField(1000)
    
    class Meta:
        db_table = 'tipo_contrato'

class Contrato(BaseModel):
    contratante = ForeignKeyField(Contratante)
    contratado = ForeignKeyField(Contratado)
    tipo = ForeignKeyField(TipoContrato)
    vigencia = DateField()
    carencia = IntegerField()
    prazo = DateField()
    valores = FloatField()
    status = CharField(20)
    datadecriacao = DateTimeField()

    class Meta:
        db_table = 'contrato'



try:    
    mysql_db.connect()
    Contratado.create_table()
    Contratante.create_table()
    TipoContrato.create_table()
    Contrato.create_table()
    mysql_db.close()
except OperationalError:   # ver na doc como capturar erro corretamente
    print("Tabela ja existe")









# import mysql.connector
# from mysql.connector import connect, Error


# try:
#     with connect(
#         host='localhost',database='contratosv1',user='ADMCOIMBRA',password='123456SETE'
#     ) as connection:
#         print(connection.get_server_info())
# except Error as e:
#     print(e)        


