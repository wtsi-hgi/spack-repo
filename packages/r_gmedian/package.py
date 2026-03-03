# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmedian(RPackage):
	"""Geometric Median, k-Medians Clustering and Robust Median PCA

	Fast algorithms for robust estimation with large samples of multivariate observations. Estimation of the geometric median, robust k-Gmedian clustering, and robust PCA based on the Gmedian covariation matrix.
	"""
	
	cran = "Gmedian" 

	version("1.2.7", md5="20e591e20776418503a6b51ef8ed5488")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
