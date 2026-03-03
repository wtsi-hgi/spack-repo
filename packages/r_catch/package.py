# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatch(RPackage):
	"""Covariate-Adjusted Tensor Classification in High-Dimensions

	Performs classification and variable selection on high-dimensional tensors (multi-dimensional arrays) after adjusting for additional covariates (scalar or vectors) as CATCH model in Pan, Mai and Zhang (2018) <arXiv:1805.04421>. The low-dimensional covariates and the high-dimensional tensors are jointly modeled to predict a categorical outcome in a multi-class discriminant analysis setting. The Covariate-Adjusted Tensor Classification in High-dimensions (CATCH) model is fitted in two steps: (1) adjust for the covariates within each class; and (2) penalized estimation with the adjusted tensor using a cyclic block coordinate descent algorithm. The package can provide a solution path for tuning parameter in the penalized estimation step. Special case of the CATCH model includes linear discriminant analysis model and matrix (or tensor) discriminant analysis without covariates.
	"""
	
	cran = "catch" 

	version("1.0.1", md5="d8cb13e7f19459cb17715da0a32cd449")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-tensr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
