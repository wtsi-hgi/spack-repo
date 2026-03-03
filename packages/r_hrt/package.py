# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHrt(RPackage):
	"""Heteroskedasticity Robust Testing

	Functions for testing affine hypotheses on the regression coefficient vector in regression models with heteroskedastic errors: (i) a function for computing various test statistics (in particular using HC0-HC4 covariance estimators based on unrestricted or restricted residuals); (ii) a function for numerically approximating the size of a test based on such test statistics and a user-supplied critical value; and, most importantly, (iii) a function for determining size-controlling critical values for such test statistics and a user-supplied significance level (also incorporating a check of conditions under which such a size-controlling critical value exists). The three functions are based on results in Poetscher and Preinerstorfer (2021) "Valid Heteroskedasticity Robust Testing" <arXiv:2104.12597>.
	"""
	
	cran = "hrt" 

	version("1.0.1", md5="58dafe8e93ab392bc30d0122178d9485")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
