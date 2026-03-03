# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpmiss(RPackage):
	"""Copula-Based Estimator for Long-Range Dependent Processes under
Missing Data

	Implements the copula-based estimator for univariate long-range dependent processes, introduced in Pumi et al. (2023) <doi:10.1007/s00362-023-01418-z>. Notably, this estimator is capable of handling missing data and has been shown to perform exceptionally well, even when up to 70% of data is missing (as reported in <arXiv:2303.04754>) and has been found to outperform several other commonly applied estimators.
	"""
	
	cran = "PPMiss" 

	version("0.1.1", md5="c92177fdaef123e33b929bdfe7aebdc6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
