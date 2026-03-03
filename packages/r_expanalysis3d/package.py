# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpanalysis3d(RPackage):
	"""Pacote Para Analise De Experimentos Com Graficos De Superficie
Resposta

	Pacote para a analise de experimentos havendo duas variaveis
    explicativas quantitativas e uma variavel dependente quantitativa. Os
    experimentos podem ser sem repeticoes ou com delineamento estatistico.
    Sao ajustados 12 modelos de regressao multipla e plotados graficos de
    superficie resposta (Hair JF, 2016) <ISBN:13:978-0138132637>.(Package
    for the analysis of experiments having two explanatory quantitative
    variables and one quantitative dependent variable. The experiments can
    be without repetitions or with a statistical design. Twelve multiple
    regression models are fitted and response surface graphs are plotted
    (Hair JF, 2016) <ISBN:13:978-0138132637>).
	"""
	
	cran = "ExpAnalysis3d" 

	version("0.1.2", md5="52192a083382629244cb9fed3a7e70fb")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
