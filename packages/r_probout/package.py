# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbout(RPackage):
	"""Unsupervised Multivariate Outlier Probabilities for Large
Datasets

	Estimates unsupervised outlier probabilities for multivariate numeric data with many observations from a nonparametric outlier statistic.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "probout" 

	version("1.1.2", md5="9dd4227c7dafdac2ba683dad199a0a74")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
