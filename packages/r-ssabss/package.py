# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsabss(RPackage):
	"""Stationary Subspace Analysis

	Stationary subspace analysis (SSA) is a blind source separation (BSS) variant where stationary components are separated from non-stationary components. Several SSA methods for multivariate time series are provided here (Flumian et al. (2021); Hara et al. (2010) <doi:10.1007/978-3-642-17537-4_52>) along with functions to simulate time series with time-varying variance and autocovariance (Patilea and Raissi(2014) <doi:10.1080/01621459.2014.884504>).
	"""
	
	cran = "ssaBSS" 

	version("0.1.1", md5="6005ae72455660fed5639ebab1fc1198")

	depends_on("r-tsbss@0.5.3:", type=("build", "run"))
	depends_on("r-ictest@0.3.4:", type=("build", "run"))
	depends_on("r-jade@2.0.2:", type=("build", "run"))
	depends_on("r-bssprep", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
