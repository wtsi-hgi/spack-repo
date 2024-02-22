# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmd(RPackage):
	"""Quantification of Multivariate Dependence

	A multivariate copula-based dependence measure. For more information, see Griessenberger, Junker, Trutschnig (2022), On a multivariate copula-based dependence measure and its estimation, Electronic Journal of Statistics, 16, 2206-2251. 
	"""
	
	cran = "qmd" 

	version("1.1.2", md5="21afbdfdcb84a79bb3e1d12855e18cd6")

	depends_on("r-qad", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
