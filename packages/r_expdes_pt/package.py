# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpdesPt(RPackage):
	"""Pacote Experimental Designs (Portugues)

	Pacote para análise de delineamentos experimentais (DIC, DBC e DQL), experimentos em esquema fatorial duplo (em DIC e DBC), experimentos em parcelas subdivididas (em DIC e DBC), experimentos em esquema fatorial duplo com um tratamento adicional (em DIC e DBC), experimentos em fatorial triplo (em DIC e DBC) e experimentos em esquema fatorial triplo com um tratamento adicional (em DIC e DBC), fazendo analise de variancia e comparacao de multiplas medias (para tratamentos qualitativos), ou ajustando modelos de regressao ate a terceira potencia (para tratamentos quantitativos); analise de residuos (Ferreira, Cavalcanti and Nogueira, 2014) <doi:10.4236/am.2014.519280>.
	"""
	
	cran = "ExpDes.pt" 

	version("1.2.2", md5="c802c030c662e106eef9ce244a743703")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stargazer", type=("build", "run"))
