# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpgmmassessment(RPackage):
	"""Optimized Automated Gaussian Mixture Assessment

	Necessary functions for optimized automated evaluation of the number and parameters of Gaussian mixtures in one-dimensional data. Various methods are available for parameter estimation and for determining the number of modes in the mixture. A detailed description of the methods ca ben found in Lotsch, J., Malkusch, S. and A. Ultsch. (2022) <doi:10.1016/j.imu.2022.101113>.
	"""
	
	cran = "opGMMassessment" 

	version("0.3.6", md5="eb55e213b63f11f649bf2cb8ff2e6b2e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-adaptgauss", type=("build", "run"))
	depends_on("r-datavisualizations", type=("build", "run"))
	depends_on("r-distributionoptimization", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mixak", type=("build", "run"))
	depends_on("r-multimode", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
