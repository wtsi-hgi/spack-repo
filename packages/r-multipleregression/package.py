# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultipleregression(RPackage):
	"""Multiple Regression Analysis

	Tools to analysis of experiments having two or more quantitative explanatory variables and one quantitative dependent variable. Experiments can be without repetitions or with a statistical design (Hair JF, 2016) <ISBN: 13: 978-0138132637>. Pacote para uma analise de experimentos havendo duas ou mais variaveis explicativas quantitativas e uma variavel dependente quantitativa. Os experimentos podem ser sem repeticoes ou com delineamento estatistico (Hair JF, 2016) <ISBN: 13: 978-0138132637>. 
	"""
	
	cran = "MultipleRegression" 

	version("0.1.0", md5="27165439f6fb820bbc4dc782391672b0")

	depends_on("r-crayon", type=("build", "run"))
