# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgwrr(RPackage):
	"""Hierarchical and Geographically Weighted Regression

	This model divides coefficients into three types,
        i.e., local fixed effects, global fixed effects, and random effects (Hu et al., 2022)<doi:10.1177/23998083211063885>.
        If data have spatial hierarchical structures (especially are overlapping on some locations),
        it is worth trying this model to reach better fitness.
	"""
	
	homepage = "https://github.com/HPDell/hgwr/"
	cran = "hgwrr" 

	version("0.3-0", md5="d8958f5c699c95e85c324eb13530cbdf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
