# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdpglm(RPackage):
	"""Hierarchical Dirichlet Process Generalized Linear Models

	Implementation of MCMC algorithms to estimate the Hierarchical Dirichlet Process Generalized Linear Model (hdpGLM) presented in the paper Ferrari (2020) Modeling Context-Dependent Latent Heterogeneity, Political Analysis <DOI:10.1017/pan.2019.13> and <doi:10.18637/jss.v107.i10>.
	"""
	
	homepage = "https://github.com/DiogoFerrari/hdpGLM"
	cran = "hdpGLM" 

	version("1.0.3", md5="64e8df6a5fd653dca6e5f637cb378121")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-ggjoy", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-isotone", type=("build", "run"))
	depends_on("r-questionr", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
