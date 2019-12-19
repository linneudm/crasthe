### Dúvidas referente as tabelas e atributos da Modelagem
1. Se vamos armazenar o XML, quais atributos deverão existir na tabela para não ser necessário consultar o XML diretamente? (Tabela Nota)
2. Vai existir venda não-fiscal?
3. Um CFOP so pode ter uma tributação?
4. Vamos usar API de Terceiros ou criar a nossa própria para o NCM? O que será necessário para obter os impostos?


### Críticas
1. Necessidade de ter uma tabela para histórico de endereço, já que esses endereços poderão ser consultados
diretamente no XML.
2. Precisaremos mesmo armazenar os dados do emitente? Criar uma tabela de configuração com os dados do emitente (ideal).
3. Armazenar Codigo IBGE e String (Cidade) e ID e String do Bairro ao invés de criar 2 tabelas.
4. Não precisa da tabela de produto_preço ja que so tera um emitente.
5. Qual a necessidade de haver uma tabela de grades? Pq nao gravar como um atributo (text), já que não iremos controlar estoque?
6. O CEP será cadastrado em banco. Utilizaremos uma API pra consultar o CEP e trazer os dados do endereço?

### Definições

- CST: Código de Situação 

- CSOSN: Código de Situação da Operação do Simples Nacional

- NCM: Nomenclatura Comum do Mercosul
    * Ex.: Água = 22011000

- IBPT: Instituto Brasileiro de Pesquisa Tributária


- CFOP: Código Fiscal de Operações e Prestações
    * Entradas: 
        - 1.000 - Entrada e/ou Aquisições de Serviços do Estado
        - 2.000 - Entrada e/ou Aquisições de outros Estados
        - 3.000 - Entrada e/ou Aquisições de Serviços do Exterior
    * Saídas:
        - 5.000 - Saídas ou Prestações de Serviços para o Estado
        - 6.000 - Saídas ou Prestações de Serviços para outros estados
        - 7.000 - Saídas ou Prestações de Serviços para o Exterior

    * CFOPs para NFCe: 5101, 5102, 5103, 5104, 5115, 5405, 5656, 5667, 5933


from django.db import connections

# Add connection information dynamically..
connections.databases['new-alias'] = { ... }
# Ensure the remaining default connection information is defined.
# EDIT: this is actually performed for you in the wrapper class __getitem__
# method.. although it may be good to do it when being initially setup to
# prevent runtime errors later.
# connections.databases.ensure_defaults('new-alias')

# Use the new connection
conn = connections['new-alias']