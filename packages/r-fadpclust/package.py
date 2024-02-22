# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFadpclust(RPackage):
	"""Functional Data Clustering Using Adaptive Density Peak Detection

	An implementation of a clustering algorithm for functional data based on adaptive density peak detection technique, in which the density is estimated by functional k-nearest neighbor density estimation based on a proposed semi-metric between functions. The proposed functional data clustering algorithm is computationally fast since it does not need iterative process. (Alex Rodriguez and Alessandro Laio (2014) <doi:10.1126/science.1242072>; Xiao-Feng Wang and Yifan Xu (2016) <doi:10.1177/0962280215609948>).
	"""
	
	cran = "FADPclust" 

	version("1.1.1", md5="23c1c7e5d88c5fe01b62d60c78c3a0af")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mfpca", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-fundata", type=("build", "run"))
