# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContaminatedmixt(RPackage):
	"""Clustering and Classification with the Contaminated Normal

	Fits mixtures of multivariate contaminated normal distributions
        (with eigen-decomposed scale matrices) via the expectation conditional-
	maximization algorithm under a clustering or classification paradigm
	Methods are described in Antonio Punzo, Angelo Mazza, and Paul D McNicholas (2018) <doi:10.18637/jss.v085.i10>.
	"""
	
	cran = "ContaminatedMixt" 

	version("1.3.8", md5="8d1b6bcc4ca019c57d9ca0d0771ad97a")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mixture", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
