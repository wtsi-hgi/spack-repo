# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCerfit(RPackage):
	"""Causal Effect Random Forest of Interaction Tress

	Fits a Causal Effect Random Forest of Interaction Tress (CERFIT) which is a modification of the Random Forest algorithm where each split is chosen to maximize subgroup treatment heterogeneity. Doing this allows it to estimate the individualized treatment effect for each observation in either randomized controlled trial (RCT) or observational data. For more information see X. Su, A. T. Peña, L. Liu, and R. A. Levine (2018) <doi:10.48550/arXiv.1709.04862>.
	"""
	
	cran = "CERFIT" 

	version("0.1.0", md5="0882a5ff5973f03978ecc918186e379a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-cbps", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
