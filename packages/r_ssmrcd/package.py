# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsmrcd(RPackage):
	"""Spatially Smoothed MRCD Estimator

	Estimation of the Spatially Smoothed Minimum Regularized Determinant (ssMRCD) estimator and its usage in an ssMRCD-based outlier detection method as described in Puchhammer and Filzmoser (2023) <doi:10.48550/arXiv.2305.05371>. Included are also complementary visualization and parameter tuning tools.
	"""
	
	cran = "ssMRCD" 

	version("0.1.0", md5="8a11fbaac4ff06d4b7e629abf2450135")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
