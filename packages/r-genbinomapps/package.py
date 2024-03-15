# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenbinomapps(RPackage):
	"""Clopper-Pearson Confidence Interval and Generalized Binomial
Distribution

	Density, distribution function, quantile function and random generation for the Generalized Binomial Distribution. Functions to compute the Clopper-Pearson Confidence Interval and the required sample size. Enhanced model for burn-in studies, where failures are tackled by countermeasures.
	"""
	
	cran = "GenBinomApps" 

	version("1.2.1", md5="fc9e7ba36d8853d8d3fb2db21a51e5fd")

