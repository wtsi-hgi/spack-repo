# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvlswimpute(RPackage):
	"""Imputation Methods for Multivariate Locally Stationary Time
Series

	Implementation of imputation techniques based on locally stationary wavelet time series forecasting methods from Wilson, R. E. et al. (2021) <doi:10.1007/s11222-021-09998-2>.
	"""
	
	cran = "mvLSWimpute" 

	version("0.1.1", md5="ab020b11d0f64d659be22aa0d5677045")

	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-mvlsw", type=("build", "run"))
	depends_on("r-binhf", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
