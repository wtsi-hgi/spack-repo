# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUbayfs(RPackage):
	"""A User-Guided Bayesian Framework for Ensemble Feature Selection

	The framework proposed in Jenul et al., (2022) <doi:10.1007/s10994-022-06221-9>, together with an interactive Shiny dashboard. 'UBayFS' is an ensemble feature selection technique embedded in a Bayesian statistical framework. The method combines data and user knowledge, where the first is extracted via data-driven ensemble feature selection. The user can control the feature selection by assigning prior weights to features and penalizing specific feature combinations. 'UBayFS' can be used for common feature selection as well as block feature selection.
	"""
	
	homepage = "https://annajenul.github.io/UBayFS/"
	cran = "UBayFS" 

	version("1.0", md5="2a4da8a783cb8b5eaac43c8729c0a005")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dirichletreg", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hyper2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mrmre", type=("build", "run"))
	depends_on("r-rdimtools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
