
"""
Modelagem feita a partir da documentação do Manual do Contribuinte
versão 6.00
http://www.nfe.fazenda.gov.br/
"""

from validators import validate_cpfcnpj

class Bairro(models.Model):
	nome = models.CharField(verbose_name='Nome do Bairro', null=False, blank=False)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING,
                             related_name='endereco', blank=False, null=False)

class Cidade(models.Model):
	"""
	Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e País).
	Informar ‘9999999‘ para operações com o exterior.
	"""
	codigo_ibge = models.IntegerField(verbose_name='Código do Município', null=False, blank=False)
	# Informar ‘EXTERIOR‘ para operações com o exterior.
	nome = models.CharField(verbose_name='Nome da Cidade', null=False, blank=False, max_length=60)
	# Informar ‘EX‘ para operações com o exterior.
	uf = models.CharField(verbose_name='UF do Município', null=False, blank=False, max_length=2)

class Endereco(models.Model):
	logradouro = models.CharField(verbose_name='Logradouro', max_length=60, null=False, blank=False)
	numero = models.CharField(verbose_name='Número', max_length=60, null=False, blank=False)
    bairro = models.ForeignKey(Bairro, models.DO_NOTHING,
                             related_name='endereco', blank=False, null=False)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING,
                             related_name='endereco', blank=False, null=False)
    # Informar os zeros não significativos.
   	cep = models.CharField(verbose_name='CEP', null=False, blank=False, max_length=8)

class Nota(models.Model):
	emitente = models.ForeignKey(Emitente, models.DO_NOTHING,
                             related_name='nota', blank=False, null=False)
	pessoa = models.ForeignKey(Pessoa, models.DO_NOTHING,
                             related_name='nota', blank=False, null=False)
	"""
	Código da UF do emitente do Documento Fiscal. Utilizar a
	Tabela do IBGE de código de unidades da federação (Anexo IX
	- Tabela de UF, Município e País).

	xml = cuf
	"""
	"""
	Código numérico que compõe a Chave de Acesso. Número
	aleatório gerado pelo emitente para cada NF-e para evitar
	acessos indevidos da NF-e. (v2.0)
	"""
	cnf = models.IntegerField(verbose_name='Código Numérico da Chave de Acesso', null=False, blank=False)
	"""
	Informar a natureza da operação de que decorrer a saída ou a
	entrada, tais como: venda, compra, transferência, devolução,
	importação, consignação, remessa (para fins de demonstração,
	de industrialização ou outra), conforme previsto na alínea 'i',
	inciso I, art. 19 do CONVÊNIO S/Nº, de 15 de dezembro de
	1970.
	"""
	nat_op = models.TextField(verbose_name='Natureza da Operação', max_length=60, null=False, blank=False)
	"""
	Série do Documento Fiscal, preencher com zeros na hipótese 
	de a NF-e não possuir série. (v2.0)
	Série 890-899: uso exclusivo para emissão de NF-e avulsa, pelo
	contribuinte com seu certificado digital, através do site do Fisco
	(procEmi=2). (v2.0)
	Serie 900-999: uso exclusivo de NF-e emitidas no SCAN. (v2.0)
	"""
	serie = models.IntegerField(verbose_name='Série do Documento Fiscal', null=False, blank=False)
	# Númer do documento fiscal
	nnf = models.IntegerField(verbose_name='Número do Documento Fiscal', null=False, blank=False)
	# Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD
	dh_emi = models.DateTimeField(verbose_name='Data e hora da emissão do documento',\
		auto_now_add=True, blank=False, null=False)
	"""
	Tipo de operação
	0 = Entrada
	1 = Saída
	"""
	tpnf = models.IntegerField(verbose_name='Tipo de Operação', null=False, blank=False)
	"""
	Identificador de local de destino da operação
	1=Operação interna;
	2=Operação interestadual;
	3=Operação com exterior.
	"""
	id_dest = models.IntegerField(verbose_name='Identificador de local de destino da operação',\
		null=False, blank=False)
	"""
	Código do Município de Ocorrência do Fato Gerador
	Informar o município de ocorrência do fato gerador do ICMS.
	Utilizar a Tabela do IBGE (Anexo IX - Tabela de UF, Município e
	País)
	"""
	c_mun_fg = models.IntegerField(verbose_name='Código do Município de Ocorrência do Fato Gerador',\
		null=False, blank=False)
	"""
	Formato de Impressão do DANFE
	0=Sem geração de DANFE;
	1=DANFE normal, Retrato;
	2=DANFE normal, Paisagem;
	3=DANFE Simplificado;
	4=DANFE NFC-e;
	5=DANFE NFC-e em mensagem eletrônica (o envio de
	mensagem eletrônica pode ser feita de forma simultânea com a
	impressão do DANFE; usar o tpImp=5 quando esta for a única
	forma de disponibilização do DANFE).
	"""
	tp_imp = models.IntegerField(verbose_name='Formato de Impressão do DANFE',\
		null=False, blank=False)
	"""
	Tipo de Emissão da NF-e
	1=Emissão normal (não em contingência);
	2=Contingência FS-IA, com impressão do DANFE em formulário
	de segurança;
	3=Contingência SCAN (Sistema de Contingência do Ambiente
	Nacional);
	4=Contingência DPEC (Declaração Prévia da Emissão em
	Contingência);
	5=Contingência FS-DA, com impressão do DANFE em
	formulário de segurança;
	6=Contingência SVC-AN (SEFAZ Virtual de Contingência do
	AN);
	7=Contingência SVC-RS (SEFAZ Virtual de Contingência do
	RS);
	9=Contingência off-line da NFC-e (as demais opções de
	contingência são válidas também para a NFC-e).
	Para a NFC-e somente estão disponíveis e são válidas as
	opções de contingência 5 e 9.
	"""
	tp_emis = models.IntegerField(verbose_name='Tipo de Emissão da NF-e',\
		null=False, blank=False)
	"""
	Informar o DV da Chave de Acesso da NF-e, o DV será
	calculado com a aplicação do algoritmo módulo 11 (base 2,9) da
	Chave de Acesso. (vide item 5 do Manual de Orientação)
	"""
	cdv = models.IntegerField(verbose_name='Dígito Verificador da Chave de Acesso da NF-e',\
		null=False, blank=False)
	"""
	Identificação do Ambiente
	1=Produção
	2=Homologação
	"""
	tp_amb = models.IntegerField(verbose_name='Identificação do Ambiente',\
		null=False, blank=False)
	"""
	Finalidade de Emissão da NF-e
	1=NF-e normal;
	2=NF-e complementar;
	3=NF-e de ajuste;
	4=Devolução de mercadoria.
	"""
	fin_nfe = models.IntegerField(verbose_name='Finalidade de emissão da NF-e',\
		null=False, blank=False)
	"""
	Indica operação com Consumidor Final
	0=Normal;
	1=Consumidor Final;
	"""
	ind_final = models.IntegerField(verbose_name='Operação com Consumidor Final',\
		null=False, blank=False)
	"""
	Indicador de presença do comprador no
	estabelecimento comercial no momento da
	operação
	0=Não se aplica (por exemplo, Nota Fiscal complementar ou de
	ajuste);
	1=Operação presencial;
	2=Operação não presencial, pela Internet;
	3=Operação não presencial, Teleatendimento;
	4=NFC-e em operação com entrega a domicílio;
	9=Operação não presencial, outros.
	"""
	ind_pres = models.IntegerField(verbose_name='Indicador de Presença do Comprador',\
		null=False, blank=False)
	"""
	Processo de emissão da NF_e
	0=Emissão de NF-e com aplicativo do contribuinte;
	1=Emissão de NF-e avulsa pelo Fisco;
	2=Emissão de NF-e avulsa, pelo contribuinte com seu
	certificado digital, através do site do Fisco;
	3=Emissão NF-e pelo contribuinte com aplicativo fornecido pelo
	Fisco
	"""
	proc_emi = models.IntegerField(verbose_name='Finalidade de emissão da NF-e',\
		null=False, blank=False)
	"""
	Versão do Processo de emissão da NF-e
	Informar a versão do aplicativo de NF-e
	"""
	ver_proc = models.CharField(verbose_name='Informar a versão do aplicativo do emissor NF-e',\
		null=False, blank=False, max_length=20)
	xml = models.TextField(verbose_name='XML da Nota', null=False, blank=False)

class Person():
	"""
	Informar o CNPJ do emitente. Na emissão de NF-e avulsa pelo
	Fisco, as informações do remetente serão informadas neste
	grupo. O CNPJ ou CPF deverão ser informados com os zeros
	não significativos.
	"""	
	cpf_cnpj = models.CharField(verbose_name='CPF', max_length=14, null=False,\
		blank=False, validators=validate_cpfcnpj)
	tipo_pessoa = models.CharField(verbose_name='Tipo Pessoa',\
		null=True, blank=True, max_length=1)
	# Razão Social ou Nome do emitente 
	nome = models.CharField(verbose_name='Nome ou Razão Social do Emitente', max_length=14, null=False)
	"""
	Preencher com o Código DDD + número do telefone. Nas
	operações com exterior é permitido informar o código do país +
	código da localidade + número do telefone (v2.0)
	"""
	fone = models.CharField(verbose_name='Fone', null=False, blank=False, max_length=14)
	### RELACIONAMENTOS
	# Obrigatório para a NF-e (modelo 55)
    endereco = models.ForeignKey(Endereco, models.DO_NOTHING,
                             related_name='pessoa', blank=False, null=False)

class PessoaFisica(Person):
	identidade_numero = models.CharField(verbose_name='Identidade Numero',\
		max_length=14, null=True, blank=True)
	identidade_orgao = models.CharField(verbose_name='Identidade Órgão',\
		max_length=14, null=True, blank=True)
	identidade_uf = models.CharField(verbose_name='Identidade UF',\
		max_length=2, null=True, blank=True)
	naturalidade = models.CharField(verbose_name='Naturalidade',\
		max_length=30, null=True, blank=True)

class PessoaJuridica(Person):
	"""
	Informar somente os algarismos, sem os caracteres de
	formatação (ponto, barra, hífen, etc.).
	Na emissão de NF-e Avulsa pode ser informado o literal
	“ISENTO” para os contribuintes do ICMS isentos de inscrição no
	Cadastro de Contribuintes de ICMS.
	"""
	inscricao_estadual = models.CharField(verbose_name='Inscrição Estadual', max_length=14, null=False)
	# Inscrição Municipal do Prestador de Serviço
	inscricao_municipal = models.CharField(verbose_name='Inscrição Municipal', max_length=15, null=False)
	# Código de regime tributário
	"""
	1=Simples Nacional;
	2=Simples Nacional, excesso sublimite de receita bruta;
	3=Regime Normal. (v2.0)
	"""
	crt = models.IntegerField(blank=False, null=False)
	nome_fantasia = models.CharField(verbose_name='Nome fantasia',\
		max_length=60, null=True, blank=True)

class Pessoa(models.Model, PessoaFisica, PessoaJuridica):
	pass

class Emitente(models.Model, PessoaFisica, PessoaJuridica):
	pass

#class Fornecedor(models.Model):
#	pass

class Produto(models.Model):
	# Origem da mercadoria
	"""
	0 - Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;
	1 - Estrangeira - Importação direta, exceto a indicada no código
	6;
	2 - Estrangeira - Adquirida no mercado interno, exceto a
	indicada no código 7;
	3 - Nacional, mercadoria ou bem com Conteúdo de Importação
	superior a 40% e inferior ou igual a 70%;
	4 - Nacional, cuja produção tenha sido feita em conformidade
	com os processos produtivos básicos de que tratam as
	legislações citadas nos Ajustes;
	5 - Nacional, mercadoria ou bem com Conteúdo de Importação
	inferior ou igual a 40%;
	6 - Estrangeira - Importação direta, sem similar nacional,
	constante em lista da CAMEX e gás natural;
	7 - Estrangeira - Adquirida no mercado interno, sem similar
	nacional, constante lista CAMEX e gás natural.
	8 - Nacional, mercadoria ou bem com Conteúdo de Importação
	superior a 70%;
	"""
	origem = models.IntegerField(verbose_name='Origem da Mercadoria', null=False, blank=False)
	"""
	Preencher com CFOP, caso se trate de itens não relacionados
	com mercadorias/produtos e que o contribuinte não possua
	codificação própria. Formato: ”CFOP9999”
	"""
	cprod = models.CharField(verbose_name='Código do Produto ou Serviço',\
		null=False, blank=False, max_length=60)
	"""
	GTIN (Global Trade Item Number) do
	produto, antigo código EAN ou código de
	barras
	Preencher com o código GTIN-8, GTIN-12, GTIN-13 ou GTIN14 
	(antigos códigos EAN, UPC e DUN-14), não informar o
	conteúdo da TAG em caso de o produto não possuir este
	código
	"""
	cean = models.CharField(verbose_name='GTIN do Produto',\
		null=False, blank=False, max_length=14)
	xprod = models.CharField(verbose_name='Descrição do Produto ou Serviço',\
		null=False, blank=False, max_length=120)
	"""
	Obrigatória informação do NCM completo (8 dígitos).
	Nota: Em caso de item de serviço ou item que não tenham
	produto (ex. transferência de crédito, crédito do ativo
	imobilizado, etc.), informar o valor 00 (dois zeros). (NT
	2014/004)
	"""
	ncm = models.IntegerField(verbose_name='Código NCM com 8 dígitos',\
		null=False, blank=False)
	cest = models.IntegerField(verbose_name='Código Especificador da Substituição Tributária',\
		null=False, blank=False)
	# Utilizar a tabela CFOP
	cfop = models.IntegerField(verbose_name='Código Fiscal de Operações e Prestações',\
		null=False, blank=False)
	# Informar a unidade de comercialização do produto
	ucom = models.CharField(verbose_name='Unidade Comercial',\
		null=False, blank=False, max_length=6)
	# Informar a quantidade de comercialização do produto (v2.0)
	qcom = models.IntegerField(verbose_name='Quantidade Comercial',\
		null=False, blank=False)
	"""
	Informar o valor unitário de comercialização do produto, campo
	meramente informativo, o contribuinte pode utilizar a precisão
	desejada (0-10 decimais). Para efeitos de cálculo, o valor
	unitário será obtido pela divisão do valor do produto pela
	quantidade comercial. (v2.0)
	"""
	v_uncom = models.DecimalField(verbose_name='Valor Unitário de comercialização',\
		null=False, blank=False, max_digits=11, decimal_places=2)
	vprod = models.DecimalField(verbose_name='Valor Total Bruto dos Produtos ou Serviços',\
		null=False, blank=False, max_digits=11, decimal_places=2)
	"""
	Preencher com o código GTIN-8, GTIN-12, GTIN-13 ou 
	GTIN14 (antigos códigos EAN, UPC e DUN-14) da unidade tributável
	do produto, não informar o conteúdo da TAG em caso de o
	produto não possuir este código.
	"""
	c_eantrib = models.IntegerField(verbose_name='GTIN da Unidade Tributável',\
		null=False, blank=False)
	utrib = models.CharField(verbose_name='Unidade Tributável',\
		null=False, blank=False, max_length=6)
	# Informar a quantidade de tributação do produto (v2.0).
	qtrib = models.IntegerField(verbose_name='Quantidade Tributável',\
		null=False, blank=False)
	"""
	Informar o valor unitário de tributação do produto, campo
	meramente informativo, o contribuinte pode utilizar a precisão
	desejada (0-10 decimais). Para efeitos de cálculo, o valor
	unitário será obtido pela divisão do valor do produto pela
	quantidade tributável (NT 2013/003).
	"""
	v_untrib = models.DecimalField(verbose_name='Valor Unitário de Tributação',\
		null=False, blank=False, max_digits=11, decimal_places=2)
	"""
	Indica se valor do Item (vProd) entra no valor total da NF-e (vProd)
	0=Valor do item (vProd) não compõe o valor total da NF-e
	1=Valor do item (vProd) compõe o valor total da NF-e (vProd) (v2.0)
	"""
	indtot = models.IntegerField(verbose_name='Indicador de Valor',\
		null=False, blank=False)
    tributacao = models.ForeignKey(Tributacao, models.DO_NOTHING,
                         related_name='produto', blank=False, null=False)
    #tributacao2 = models.ForeignKey(Tributacao2, models.DO_NOTHING,
    #                     related_name='produto', blank=False, null=False)

class NotaItem(models.Model):
	descricao = models.CharField(verbose_name='Descrição', null=True, blank=True, max_length=120)
	quantidade = models.IntegerField(verbose_name='Quantidade',\
		null=False, blank=False)
	num_lote = models.IntegerField(verbose_name='Quantidade',\
		null=False, blank=False)
	nota = models.ForeignKey(Nota, related_name='notaitem')
	produto = models.ForeignKey(Produto, related_name='notaitem')

class CFOP(models.Model):
	descricao = models.CharField(verbose_name='Descrição', null=False, blank=False, max_length=255)
	descricao_completa = models.TextField(verbose_name='Descrição', null=True, blank=True)

class Tributacao(models.Model):
	grupo = models.IntegerField(verbose_name='Grupo de Tributação', null=False, blank=False)
	cst = models.IntegerField(verbose_name='Tributação do ICMS', blank=False, null=False)
	"""
	0=Margem Valor Agregado (%);
	1=Pauta (Valor);
	2=Preço Tabelado Máx. (valor);
	3=Valor da operação
	"""
	mod_bc = models.IntegerField(verbose_name='Modalidade de determinação da BC do ICMS',\
		null=False, blank=False)
	v_bc = models.DecimalField(verbose_name='Valor da BC do ICMS',\
		null=False, blank=False, max_digits=13, decimal_places=2)
	picms = models.DecimalField(verbose_name='Alíquota do Imposto',\
		null=False, blank=False, max_digits=10, decimal_places=2)
	vicms = models.DecimalField(verbose_name='Valor do ICMS',\
		null=False, blank=False, max_digits=10, decimal_places=2)
	"""
	0=Preço tabelado ou máximo sugerido;
	1=Lista Negativa (valor);
	2=Lista Positiva (valor);
	3=Lista Neutra (valor);
	4=Margem Valor Agregado (%);
	5=Pauta (valor);
	"""
	mod_bcst = models.IntegerField(verbose_name='Modalidade de determinação da BC do ICMS ST',\
		null=True, blank=True)
	v_bcst = models.DecimalField(verbose_name='Valor da BC do ICMS ST',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	p_icmsst = models.DecimalField(verbose_name='Alíquota do imposto do ICMS ST',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	# Valor do ICMS ST retido
	v_icmsst = models.DecimalField(verbose_name='Valor do ICMS ST',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	v_icmsdeson = models.DecimalField(verbose_name='Valor do ICMS Desonerado',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	mot_desicms = models.IntegerField(verbose_name='Motivo da desoneração do ICMS',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	"""
	Valor da BC do ICMS ST cobrado anteriormente por ST (v2.0).
	O valor pode ser omitido quando a legislação não exigir a sua
	informação. (NT 2011/004)
	"""
	v_bcstret = models.DecimalField(verbose_name='Valor da BC do ICMS ST Retido',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	"""
	Valor do ICMS ST cobrado anteriormente por ST (v2.0). O valor
	pode ser omitido quando a legislação não exigir a sua
	informação. (NT 2011/004)
	"""
	v_icmsstret = models.DecimalField(verbose_name='Valor do ICMS ST Retido',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	""" 
	Percentual para determinação do valor da Base de 
	Cálculo da operação própria. (v2.0)
	"""
	p_bcop = models.DecimalField(verbose_name='Percentual da BC operação própria',\
		null=True, blank=True, max_digits=3, decimal_places=4)
	"""
	Sigla da UF para qual é devido o ICMS ST da operação.
	Informar "EX" para Exterior. (v2.0)
	"""
	ufst = models.CharField(verbose_name='UF para qual é devido o ICMS ST',\
		null=True, blank=True, max_length=2)
	"""
	Código de Situação da Operação – Simples Nacional
	101=Tributada pelo Simples Nacional com permissão de
	crédito. (v2.0)
	"""
	c_sosn = models.IntegerField(verbose_name='Código de Situação da Operação',\
		null=True, blank=True)
	p_credsn = models.DecimalField(verbose_name='Alíquota aplicável de cálculo do crédito',\
		null=True, blank=True, max_digits=3, decimal_places=4)
	"""
	Valor crédito do ICMS que pode ser
	aproveitado nos termos do art. 23 da LC
	123 (Simples Nacional)
	"""
	v_credicmmssn = models.DecimalField(verbose_name='Valro crédito do ICMS',\
		null=True, blank=True, max_digits=13, decimal_places=2)
	cfop = models.ForeignKey(CFOP, related_name='tributacao')

