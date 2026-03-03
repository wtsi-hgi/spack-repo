# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMecoturn(RPackage):
	"""Decipher Microbial Turnover along a Gradient

	Two pipelines are provided to study microbial turnover along a gradient, including the beta diversity and microbial abundance change. The 'betaturn' class consists of the steps of community dissimilarity matrix generation, matrix conversion, differential test and visualization. The workflow of 'taxaturn' class includes the taxonomic abundance calculation, abundance transformation, abundance change summary, statistical analysis and visualization. Multiple statistical approaches can contribute to the analysis of microbial turnover.
	"""
	
	homepage = "https://github.com/ChiLiubio/mecoturn"
	cran = "mecoturn" 

	version("0.3.0", md5="89a917e32da0e8ed6d6a1e8155fc724e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-microeco@0.20:", type=("build", "run"))
	depends_on("r-gunifrac", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
