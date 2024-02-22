# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpsvarapprox(RPackage):
	"""Approximate the Variance of the Horvitz-Thompson Total Estimator

	Variance approximations for the 
    Horvitz-Thompson total estimator in Unequal Probability Sampling
    using only first-order inclusion probabilities. 
    See Matei and Tillé (2005) and Haziza, Mecatti and Rao (2008) for details.
	"""
	
	cran = "UPSvarApprox" 

	version("0.1.4", md5="c70cc49522ea0628cdf72be7f6c064b8")

