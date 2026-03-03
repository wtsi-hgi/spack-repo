# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmnetcr(RPackage):
	"""Fit a Penalized Constrained Continuation Ratio Model for
Predicting an Ordinal Response

	Penalized methods are useful for fitting over-parameterized models. This package includes functions for restructuring an ordinal
 response dataset for fitting continuation ratio models for datasets  where the number of covariates exceeds the sample size or when
 there is collinearity among the covariates. The 'glmnet' fitting algorithm is used to fit the continuation ratio model after data restructuring.
	"""
	
	cran = "glmnetcr" 

	version("1.0.6", md5="2721c37fe164f61cb628771867145b43")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
