# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnetlts(RPackage):
	"""Robust and Sparse Methods for High Dimensional Linear and Binary
and Multinomial Regression

	Fully robust versions of the elastic net estimator are introduced for linear and binary and multinomial regression, in particular high dimensional data. The algorithm searches for outlier free subsets on which the classical elastic net estimators can be applied. A reweighting step is added to improve the statistical efficiency of the proposed estimators. Selecting appropriate tuning parameters for elastic net penalties are done via cross-validation. 
	"""
	
	cran = "enetLTS" 

	version("1.1.0", md5="e261918a1d2246dddf41cbb2a10a87cd")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-robusthd", type=("build", "run"))
