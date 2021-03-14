from dbmodel import *



# Contratado.create(razao_social ='Atila ltda',
#                     endereco ='Pinheiro machado',
#                     cnpj ='12345678901234', 
#                     telefone ='69984492828')


# Contratante.create(razao_social ='luisa ltda',
#                     endereco ='Pinheiro machado',
#                     cnpj ='12345678901234', 
#                     telefone ='69984492828')

# TipoContrato.create(tipo ='Emprestimo',
#                     objeto = 'Objeto do contrato emprestimo')

# TipoContrato.create(tipo ='Arrendamento',
#                     objeto = 'Objeto do contrato de Arrendamento')

# TipoContrato.create(tipo ='Seguro',
#                     objeto = 'Objeto do contrato de Seguro')

# TipoContrato.create(tipo ='Locação de Serviços e Equipamentos',
#                     objeto = 'Objeto do contrato de Locação de Serviços e Equipamentos')



#Contrato.create(contratante = '1', contratado = '1', tipo ='3', vigencia ='2001-09-28', carencia ='10',
#                 prazo ='2002-10-28', valores ='280,50', status ='Ativo', datadecriacao ='2001-02-01 20:02:23')


######################
# TESTANDO MEUS GETS #
######################

contratado = Contratado.get(Contratado.id == "1").get()
print('Razão Social ={}. Endereço do Contratado ={}. CNPJ = {}. Telefone = {}'.format(contratado.razao_social, contratado.endereco, contratado.cnpj, contratado.telefone))

tipocontrato = TipoContrato.get(TipoContrato.id == "3").get()
print('Tipo de Contrato ={}. Qual o objeto = {} '.format(tipocontrato.tipo, tipocontrato.objeto))

tiposcontrato = TipoContrato.select(TipoContrato.tipo, TipoContrato.objeto)

for tipo in tiposcontrato:
    print('Tipo de Contrato ={}.objeto = {} '.format(tipo.tipo, tipo.objeto))


contrato = Contrato.select().where(Contrato.status == "Ativo")
#print('Data da vigência = {}. Carencia = {}. Prazo = {}. Valor = {}. Status = {}. Data da Criação = {} '.format(contrato.vigencia, contrato.carencia, contrato.prazo, contrato.valores, contrato.status, contrato.datadecriacao))

for item in contrato:
    print('Data da vigência = {}. Carencia = {}. Prazo = {}. Valor = {}. Status = {}. Data da Criação = {} '.format(item.vigencia, item.carencia, item.prazo, item.valores, item.status, item.datadecriacao))
