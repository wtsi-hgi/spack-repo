# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmeinfo(RPackage):
	"""Information Matrices for 'lmeStruct' and 'glsStruct' Objects

	Provides analytic derivatives and information matrices for
    fitted linear mixed effects (lme) models and generalized least squares (gls) models
    estimated using lme() (from package 'nlme') and gls() (from package 'nlme'), respectively.
    The package includes functions for estimating the sampling variance-covariance of variance
    component parameters using the inverse Fisher information. The variance components include
    the parameters of the random effects structure (for lme models), the variance structure,
    and the correlation structure. The expected and average forms of the Fisher information matrix
    are used in the calculations, and models estimated by full maximum likelihood or
    restricted maximum likelihood are supported. The package also includes a function for estimating
    standardized mean difference effect sizes (Pustejovsky, Hedges, and Shadish (2014) <DOI:10.3102/1076998614547577>)
    based on fitted lme or gls models.
	"""
	
	homepage = "https://jepusto.github.io/lmeInfo/"
	cran = "lmeInfo" 

	version("0.3.2", md5="87f79a1fb85cf9980075283dcd421b41")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
