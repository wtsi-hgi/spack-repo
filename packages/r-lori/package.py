# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLori(RPackage):
	"""Imputation of High-Dimensional Count Data using Side Information

	Analysis, imputation, and multiple imputation of count data using covariates. LORI uses a log-linear Poisson model where main row and column effects, as well as effects of known covariates and interaction terms can be fitted. The estimation procedure is based on the convex optimization of the Poisson loss penalized by a Lasso type penalty and a nuclear norm. LORI returns estimates of main effects, covariate effects and interactions, as well as an imputed count table. The package also contains a multiple imputation procedure. The methods are described in Robin, Josse, Moulines and Sardy (2019) <arXiv:1703.02296v4>.
	"""
	
	cran = "lori" 

	version("2.2.2", md5="7a52228b19e85587c8b0badbcb759153")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
