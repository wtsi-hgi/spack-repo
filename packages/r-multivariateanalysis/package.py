# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultivariateanalysis(RPackage):
	"""Pacote Para Analise Multivariada

	Package with multivariate analysis methodologies for experiment evaluation.
	 The package estimates dissimilarity measures, builds dendrograms, obtains MANOVA,
	 principal components, canonical variables, etc. (Pacote com metodologias de analise
	 multivariada para avaliação de experimentos. O pacote estima medidas de dissimilaridade,
	 construi de dendogramas, obtem a MANOVA,  componentes principais, variáveis canônicas, etc.)
	"""
	
	cran = "MultivariateAnalysis" 

	version("0.4.4", md5="34008d2cbbc33ea04b9b7150799e5dec")

	depends_on("r-pcamixdata", type=("build", "run"))
	depends_on("r-candisc", type=("build", "run"))
	depends_on("r-biotools", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
