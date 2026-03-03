# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcfmperiod(RPackage):
	"""Robust Estimation of the ACF from the M-Periodogram

	Non-robust and robust computations of the sample autocovariance (ACOVF) and sample autocorrelation functions (ACF) of univariate and multivariate processes. The methodology consists in reversing the diagonalization procedure involving the periodogram or the cross-periodogram and the Fourier transform vectors, and, thus, obtaining the ACOVF or the ACF as discussed in Fuller (1995) <doi:10.1002/9780470316917>. The robust version is obtained by fitting robust M-regressors to obtain the M-periodogram or M-cross-periodogram as discussed in Reisen et al. (2017) <doi:10.1016/j.jspi.2017.02.008>.
	"""
	
	cran = "acfMPeriod" 

	version("1.0.0", md5="ddc0c9a86eb7c1a2955510e3979addc9")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
