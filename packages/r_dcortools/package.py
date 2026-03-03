# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcortools(RPackage):
	"""Providing Fast and Flexible Functions for Distance Correlation
Analysis

	Provides methods for distance covariance and distance correlation (Szekely, et al. (2007) <doi:10.1214/009053607000000505>), generalized version thereof (Sejdinovic, et al. (2013) <doi:10.1214/13-AOS1140>) and corresponding tests (Berschneider, Bottcher (2018) <arXiv:1808.07280>. Distance standard deviation methods (Edelmann, et al. (2020) <doi:10.1214/19-AOS1935>) and distance correlation methods for survival endpoints (Edelmann, et al. (2021) <doi:10.1111/biom.13470>) are also included.
	"""
	
	cran = "dcortools" 

	version("0.1.6", md5="80af220e27402bca5bae29f648ccdc30")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
