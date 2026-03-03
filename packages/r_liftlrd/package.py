# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiftlrd(RPackage):
	"""Wavelet Lifting Estimators of the Hurst Exponent for Regularly
and Irregularly Sampled Time Series

	Implementations of Hurst exponent estimators based on the relationship between wavelet lifting scales and wavelet energy of Knight et al (2017) <doi:10.1007/s11222-016-9698-2>. 
	"""
	
	cran = "liftLRD" 

	version("1.0-9", md5="cb7f6ab3ddd7c233ee2ba9c37273a0d7")

	depends_on("r-adlift", type=("build", "run"))
	depends_on("r-nlt", type=("build", "run"))
