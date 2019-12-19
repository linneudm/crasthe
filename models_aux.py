# Classe gerada obtendo as informações do banco de dados do PlusPDV
class Tribuatacao2(models.Model):
	uf = models.CharField(verbose_name='UF', null=False, blank=False, max_length=2)
	cst_icms = models.IntegetField(null=True, blank=True)
	mod_bc_icms = models.IntegetField(null=True, blank=True)
	aliquota_icms = DecimalField(verbose_name='Aliquota do ICMS',\
		null=True, blank=True, max_digits=6, decimal_places=2)
	csosn = models.IntegetField(null=True, blank=True)
	aliquota_simples_nacional = DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
	aliquota_fcp = DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
	cst_ipi = models.IntegetField(null=True, blank=True)
	codigo_ipi = models.IntegetField(null=True, blank=True)
	aliquota_ipi = DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
	cst_pis = models.IntegetField(null=True, blank=True)
	aliquota_pis = DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
	cst_confins = models.IntegetField(null=True, blank=True)
	aliquota_confins = DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
	mva_inteirno = DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
	aliquota_iss = DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)

