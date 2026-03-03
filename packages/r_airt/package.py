# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirt(RPackage):
	"""Evaluation of Algorithm Collections Using Item Response Theory

	An evaluation framework for algorithm portfolios using Item Response
    Theory (IRT). We use continuous and polytomous IRT models to evaluate algorithms and introduce
    algorithm characteristics such as stability, effectiveness and anomalousness 
    (Kandanaarachchi, Smith-Miles 2020) <doi:10.13140/RG.2.2.11363.09760>.
	"""
	
	homepage = "https://sevvandi.github.io/airt/"
	cran = "airt" 

	version("0.2.2", md5="a6903b86c703cbfb9d50151340163df8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-estcrm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
