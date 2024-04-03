# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdrt(RPackage):
	"""Estimating the Sufficient Dimension Reduction Subspaces in Time
Series

	The sdrt() function is designed for estimating subspaces for Sufficient Dimension Reduction (SDR) in time series, with a specific focus on the Time Series Central Mean subspace (TS-CMS). The package employs the Fourier transformation method proposed by Samadi and De Alwis (2023) <doi:10.48550/arXiv.2312.02110> and the Nadaraya-Watson kernel smoother method proposed by Park et al. (2009) <doi:10.1198/jcgs.2009.08076> for estimating the TS-CMS. The package provides tools for estimating distances between subspaces and includes functions for selecting model parameters using the Fourier transformation method. 
	"""
	
	cran = "sdrt" 

	version("1.0.0", md5="05c8467d8954cc4631ac8d21ff47a05e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
