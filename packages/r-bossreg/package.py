# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBossreg(RPackage):
	"""Best Orthogonalized Subset Selection (BOSS)

	Best Orthogonalized Subset Selection (BOSS) is a least-squares (LS) based subset selection method, that performs best subset selection upon an orthogonalized basis of ordered predictors, with the computational effort of a single ordinary LS fit. This package provides a highly optimized implementation of BOSS and estimates a heuristic degrees of freedom for BOSS, which can be plugged into an information criterion (IC) such as AICc in order to select the subset from candidates. It provides various choices of IC, including AIC, BIC, AICc, Cp and GCV. It also implements the forward stepwise selection (FS) with no additional computational cost, where the subset of FS is selected via cross-validation (CV). CV is also an option for BOSS. For details see: Tian, Hurvich and Simonoff (2021), "On the Use of Information Criteria for Subset Selection in Least Squares Regression", <arXiv:1911.10191>.
	"""
	
	homepage = "https://github.com/sentian/BOSSreg"
	cran = "BOSSreg" 

	version("0.2.0", md5="e9da826e6c719370868b7f66f1432971")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
