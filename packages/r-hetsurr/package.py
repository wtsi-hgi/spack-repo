# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHetsurr(RPackage):
	"""Assessing Heterogeneity in the Utility of a Surrogate Marker

	Provides a function to assess and test for heterogeneity in the utility of a surrogate marker with respect to a baseline covariate. The main function can be used for either a continuous or discrete baseline covariate. More details will be available in the future in: Parast, L., Cai, T., Tian L (2021). "Testing for Heterogeneity in the Utility of a Surrogate Marker." Biometrics, In press.
	"""
	
	cran = "hetsurr" 

	version("1.0", md5="974a2ee6965b2400738f05efadcaaa43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsurrogate", type=("build", "run"))
