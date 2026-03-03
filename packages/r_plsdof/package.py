# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsdof(RPackage):
	"""Degrees of Freedom and Statistical Inference for Partial Least
Squares Regression

	The plsdof package provides Degrees of Freedom estimates
        for Partial Least Squares (PLS) Regression. Model selection for
        PLS is based on various information criteria (aic, bic, gmdl)
        or on cross-validation. Estimates for the mean and covariance
        of the PLS regression coefficients are available. They allow
        the construction of approximate confidence intervals and the
        application of test procedures (Kramer and Sugiyama 
        2012 <doi:10.1198/jasa.2011.tm10107>).
        Further, cross-validation procedures for Ridge Regression and 
        Principal Components Regression are available.
	"""
	
	homepage = "https://github.com/fbertran/plsdof/"
	cran = "plsdof" 

	version("0.3-2", md5="eb1152cbb3d93b2a940532cb568262d1")

	depends_on("r-mass", type=("build", "run"))
