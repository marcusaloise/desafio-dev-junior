# Arquitetura

## Plano de ação

### Tecnologias:

- Banco de dados Relacional --> MySql
- Linguagem --> Python 
- Deploy --> Docker 

### Features - backend:

- Validador de CNPJ 
- Pegar endereço pelo CEP 
- Validador de Telefone 
- Criar contrato [OK]
- cadastro do contratante [OK] 
- cadastro do tipo do contratado [OK]
- cadastro do tipo do contrato [OK]
- Atualizar contrato [OK]
- Deletar contrato [OK]
- Buscar contrato[OK]
- manter as credencias do db de forma segura 

#### Regra de Negocio 

- O contrato so pode ser deletado se estiver com o status "cancelado"
- Data de criação do contrato 


### Features - Frontend:

* Tela de Login
- Tela incial 
    - Pesquisa por Dados do Contratante/Contratado; Vigência; Prazos; Valores; Status.
    - Acesso ao cadastro de contratantes 
    - Acesso ao cadastro de contratado 
    - Acesso ao cadastro de tipo de contrato
    - Acesso ao cadastro de contrato 

- Tela de cadastro de contratante 
    - Formulario de cadastro
        - Razão social 
        - endereco 
        - cnpj 
        - telefone

- Tela de cadastro do contratado
    - Formulario de cadastro
        - Razão social 
        - endereco 
        - cnpj 
        - telefone

- Tela de cadastro do tipo de contrato 
    - Tipo [Empréstimos, Arrendamento, Seguro e Locação de Serviços e Equipamentos.]
    - Objeto

- Tela de cadastro de contrato 
    - Tipo (seletor Drop down)
    - Contratante (Pesquisa de auto complete)
    - Contratado (Pesquisa de auto complete)
    - Vigência (Seletor de Datas)
    - Carência (Campo)
    - Prazo (Seleto de Datas)
    - Valores (Campo)
    - Status (Seletor Drop Down)







Contratante: Dados da empresa: Razão Social, CNPJ, Endereço e telefone;
Contratado: Dados da instituição ou empresa que ofertará o serviço: Razão Social, CNPJ, Endereço, telefone;
Objeto: Tipo do Contrato;
Condições Financeiras: carência, vigência, valores e prazos.
Status: Em Edição, Ativo, Cancelado.
Almeja que seja possível fazer o cadastro (CRUD) dos contratos, de acordo com os tipos, informando Dados do Contratante, Contratado, vigência, prazos e valores. Sendo que ao cadastrar um novo contrato, este seja iniciado no status em edição.

Deseja também uma opção para busca, listagem e detalhamento dos Contratos. Este detalhamento deve exibir:

Dados do Contratante/Contratado;
Vigência;
Prazos;
Valores;
Status.
Sendo possível filtrar por contratado, vigência, data de inserção e status.
### Modelo Banco de Dados:

- Tabela contratantes: [OK]
    - contratante_ID (pkey)
    - razao_social (string)
    - endereco (string)
    - cnpj (int)
    - telefone (int)

- Tabela contratado: [OK]
    - contratado_ID (pkey)
    - razão_social (string)
    - endereco (string)
    - cnpj (int)
    - telefone (int)

- Tabela tipo_contrato: [OK]
    - tipo_contrato_ID (pkey)
    - tipo [Empréstimos|Arrendamento|Seguro|Locação de Serviços e Equipamentos] (string)
    - objeto do contrato (string)


- Tabela contratos: [OK]
    - contrato_ID (pkey)
    - tipo_ID (fkey)
    - contratante_ID (fkey) 
    - contratado_ID (fkey)
    - vigencia (date)
    - carencia (dias)
    - prazos (date)
    - valores (real)
    - status [Edição|Ativo|Cancelado] (string)


