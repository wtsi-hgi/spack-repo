# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliftlrd(RPackage):
	"""Complex-Valued Wavelet Lifting Estimators of the Hurst Exponent
for Irregularly Sampled Time Series

	Implementation of Hurst exponent estimators based on complex-valued lifting wavelet energy from Knight, M. I and Nunes, M. A. (2018) <doi:10.1007/s11222-018-9820-8>. 
	"""
	
	cran = "CliftLRD" 

	version("0.1-1", md5="16e4548a353f87e263c1d97fef60caae")

	depends_on("r-cnltreg", type=("build", "run"))
	depends_on("r-liftlrd", type=("build", "run"))
