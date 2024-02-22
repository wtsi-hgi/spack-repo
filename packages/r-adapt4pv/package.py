# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdapt4pv(RPackage):
	"""Adaptive Approaches for Signal Detection in Pharmacovigilance

	A collection of several pharmacovigilance signal detection methods based on adaptive lasso. Additional lasso-based and propensity score-based signal detection approaches are also supplied. See Courtois et al <doi:10.1186/s12874-021-01450-3>.
	"""
	
	cran = "adapt4pv" 

	version("0.2-3", md5="ed78228d095160429c0bd67d4ebf36a4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.0.6:", type=("build", "run"))
	depends_on("r-glmnet@3.0.2:", type=("build", "run"))
	depends_on("r-speedglm", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
