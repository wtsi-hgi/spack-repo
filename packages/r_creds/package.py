# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCreds(RPackage):
	"""Calibrated Ratio Estimator under Double Sampling Design

	Population ratio estimator (calibrated) under two-phase random sampling design has gained enormous popularity in the recent time. This package provides functions for estimation population ratio (calibrated) under two phase sampling design, including the approximate variance of the ratio estimator. The improved ratio estimator can be applicable for both the case, when auxiliary data is available at unit level or aggregate level (eg., mean or total) for first phase sampled. Calibration weight of each unit of the second phase sample was calculated. Single and combined inclusion probabilities were also estimated for both phases under two phase random [simple random sampling without replacement (SRSWOR)] sampling. The improved ratio estimator's percentage coefficient of variation was also determined as a measure of accuracy. This package has been developed based on the theoretical development of Islam et al. (2021) and Ozgul (2020) <doi:10.1080/00949655.2020.1844702>.
	"""
	
	cran = "CREDS" 

	version("0.1.0", md5="5d9e267a6f99a55b8a5586e9b992701e")

	depends_on("r-mass", type=("build", "run"))
