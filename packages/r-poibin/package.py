# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoibin(RPackage):
	"""The Poisson Binomial Distribution

	Implementation of both the exact and approximation methods for computing the cdf of the Poisson binomial distribution as described in Hong (2013) <doi: 10.1016/j.csda.2012.10.006>. It also provides the pmf, quantile function, and random number generation for the Poisson binomial distribution. The C code for fast Fourier transformation (FFT) is written by R Core Team (2019)<https://www.R-project.org/>, which implements the FFT algorithm in Singleton (1969) <doi: 10.1109/TAU.1969.1162042>.
	"""
	
	cran = "poibin" 

	version("1.5", md5="ccb27983b15b6670ae4b454bea9bd0a1")


	def setup_build_environment(self, env):
		# Define PI to satisfy code using bare PI macro
		pi_define = '-DPI=3.141592653589793238462643383279502884197'
		env.append_flags('CPPFLAGS', pi_define)
		env.append_flags('PKG_CPPFLAGS', pi_define)
		env.append_flags('CFLAGS', pi_define)

