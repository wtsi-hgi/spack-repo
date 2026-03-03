# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsingfit(RPackage):
	"""Fitting Ising Models Using the ELasso Method

	This network estimation procedure eLasso, which is based on the Ising model, combines l1-regularized logistic regression with model selection based on the Extended Bayesian Information Criterion (EBIC). EBIC is a fit measure that identifies relevant relationships between variables. The resulting network consists of variables as nodes and relevant relationships as edges. Can deal with binary data.
	"""
	
	cran = "IsingFit" 

	version("0.4", md5="d178f6733aaf2d2c90925442c8efe7c2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
