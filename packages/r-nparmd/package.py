# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNparmd(RPackage):
	"""Nonparametric Analysis of Multivariate Data in Factorial Designs

	Analysis of multivariate data with two-way completely randomized
    factorial design. The analysis is based on fully nonparametric, rank-based
    methods and uses test statistics based on the Dempster's ANOVA, Wilk's Lambda,
    Lawley-Hotelling and Bartlett-Nanda-Pillai criteria. The multivariate
    response is allowed to be ordinal, quantitative, binary or a mixture of the
    different variable types. The package offers two functions performing the
    analysis, one for small and the other for large sample sizes. The underlying methodology
    is largely described in Bathke and Harrar (2016) <doi:10.1007/978-3-319-39065-9_7> and in 
    Munzel and Brunner (2000) <doi:10.1016/S0378-3758(99)00212-8>.
	"""
	
	cran = "nparMD" 

	version("0.2.1", md5="bbe358cbb28098e8924b2605a91eacd8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
