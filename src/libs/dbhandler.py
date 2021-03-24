from dbmodel import *



# Contratado.create(razao_social ='Maria helena',
#                     endereco ='São cristpvão',
#                     cnpj ='59876245836987', 
#                     telefone ='6987526348')


# Contratante.create(razao_social ='Jesus cristo',
#                     endereco ='Aponiã',
#                     cnpj ='35629875168954', 
#                     telefone ='5689742685')


# Contratado.create(razao_social ='lilu',
#                     endereco ='Sapiens',
#                     cnpj ='69583214569873', 
#                     telefone ='5623495876')


# Contratante.create(razao_social ='Laura',
#                     endereco ='Caxias',
#                     cnpj ='12346598754264', 
#                     telefone = "6953214568")


# Contratado.create(razao_social ='Alberto',
#                     endereco ='Curitiba',
#                     cnpj ='65987426531548', 
#                     telefone ='6935987621')


# Contratante.create(razao_social ='Edite',
#                     endereco ='Pinhais',
#                     cnpj ='12365498785264', 
#                     telefone = '6985234659' )


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

##############
# update #####
##############

# res = (Contratante
#        .update(razao_social="João Pedro")
#        .where(Contratante.id == 1)
#        .execute())

# res = (Contratado
#        .update(telefone = 6998892828)
#        .where(Contratado.cnpj == 12345678901234)
#        .execute())

# res = (TipoContrato
#        .update(objeto = "Novo objeto" )
#        .where(TipoContrato.tipo == "Arrendamento" )
#        .execute())

# res = (Contrato
#        .update(tipo = 4 )
#        .where(Contrato.id == 2 )
#        .execute())


# res = (Contrato
#        .update(contratante = 3 )
#        .where(Contrato.id == 1 )
#        .execute())

# res = (Contrato
#        .update(contratado = 2 )
#        .execute())

# res = (Contrato
#        .update(vigencia = '2002-03-19' )
#        .where(Contrato.id == 2 )
#        .execute())

# res = (Contrato
#        .update(carencia = 18)
#        .where(Contrato.id == 2 )
#        .execute())
       
# res = (Contrato
#        .update(valores = 270.7 )
#        .where(Contrato.id == 2 )
#        .execute())

# res = (Contrato
#        .update(status = 'Inativo' )
#        .where(Contrato.id == 2 )
#        .execute())


##############
# Delete #####
##############


# res = (Contrato
#        .delete()
#        .where(Contrato.id == 2 )
#        .execute())


# res = (Contratante
#        .delete()
#        .where(Contratante.id == 3 )
#        .execute())
