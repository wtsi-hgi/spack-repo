# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetanb(RPackage):
	"""Bootstrap for Regression Effect Sizes

	Generates nonparametric bootstrap confidence intervals
    (Efron & Tibshirani, 1993: <doi:10.1201/9780429246593>)
    for standardized regression coefficients (beta) and other effect sizes,
    including multiple correlation, semipartial correlations,
    improvement in R-squared, squared partial correlations,
    and differences in standardized regression coefficients,
    for models fitted by lm().
	"""
	
	homepage = "https://github.com/jeksterslab/betaNB"
	cran = "betaNB" 

	version("1.0.3", md5="4889e37766ab22606d57cf713879f427")

	depends_on("r@3.5:", type=("build", "run"))
