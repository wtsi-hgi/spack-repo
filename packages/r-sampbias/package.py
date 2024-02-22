# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSampbias(RPackage):
	"""Evaluating Geographic Sampling Bias in Biological Collections

	Evaluating the biasing impact of geographic features such as airports, cities, roads, rivers in datasets of coordinates based biological collection datasets, by Bayesian estimation of the parameters of a Poisson process. Enables also spatial visualization of sampling bias and includes a set of convenience functions for publication level plotting. Also available as 'shiny' app. The reference for the methodology is: Zizka et al. (2020) <doi:10.1111/ecog.05102>.
	"""
	
	homepage = "https://github.com/azizka/sampbias"
	cran = "sampbias" 

	version("2.0.0", md5="d9305eac24f2b4e6b0b6de11030fbbca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
