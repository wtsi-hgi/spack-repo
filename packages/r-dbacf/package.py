# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbacf(RPackage):
	"""Autocovariance Estimation via Difference-Based Methods

	Provides methods for (auto)covariance/correlation function estimation 
    in change point regression with stationary errors circumventing the pre-estimation
    of the underlying signal of the observations. Generic, first-order, (m+1)-gapped,
    difference-based autocovariance function estimator is based on M. Levine and I. Tecuapetla-Gómez (2023) <doi:10.48550/arXiv.1905.04578>. Bias-reducing, second-order, (m+1)-gapped, 
    difference-based estimator is based on I. Tecuapetla-Gómez and A. Munk (2017) 
    <doi:10.1111/sjos.12256>. Robust autocovariance estimator for change point regression with autoregressive errors is based on S. Chakar et al. (2017) <doi:10.3150/15-BEJ782>. 
    It also includes a general projection-based method for covariance matrix estimation.
	"""
	
	cran = "dbacf" 

	version("0.2.8", md5="aeffa943a6b11a49f2d5121e90249ca5")

	depends_on("r@2.15.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
