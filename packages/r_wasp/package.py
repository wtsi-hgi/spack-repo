# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWasp(RPackage):
	"""Wavelet System Prediction

	The wavelet-based variance transformation method is used for system modelling and prediction. It refines predictor spectral representation using Wavelet Theory, which leads to improved model specifications and prediction accuracy. Details of methodologies used in the package can be found in Jiang, Z., Sharma, A., & Johnson, F. (2020) <doi:10.1029/2019WR026962>, Jiang, Z., Rashid, M. M., Johnson, F., & Sharma, A. (2020) <doi:10.1016/j.envsoft.2020.104907>, and Jiang, Z., Sharma, A., & Johnson, F. (2021) <doi:10.1016/J.JHYDROL.2021.126816>.
	"""
	
	homepage = "https://github.com/zejiang-unsw/WASP#readme"
	cran = "WASP" 

	version("1.4.3", md5="bc0b61fb8c5177f81dae1ebdae0231d5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
