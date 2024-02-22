# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGscalca(RPackage):
	"""Generalized Structure Component Analysis- Latent Class Analysis
& Latent Class Regression

	
    Execute Latent Class Analysis (LCA) and Latent Class Regression (LCR) by using Generalized Structured Component Analysis (GSCA). This is explained in Ryoo, Park, and Kim (2019) <doi:10.1007/s41237-019-00084-6>.
    It estimates the parameters of latent class prevalence and item response probability in LCA with a single line comment. It also provides graphs of item response probabilities. In addition, the package enables to estimate the relationship between the prevalence and covariates. 
	"""
	
	homepage = "https://github.com/hee6904/gscaLCA"
	cran = "gscaLCA" 

	version("0.0.5", md5="c7d88b37b8c1102f7cd96bc3637a6c57")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-fclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
