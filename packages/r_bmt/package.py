# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmt(RPackage):
	"""The BMT Distribution

	Density, distribution, quantile function, random number generation for the BMT (Bezier-Montenegro-Torres) distribution. Torres-Jimenez C.J. and Montenegro-Diaz A.M. (2017) <arXiv:1709.05534>. Moments, descriptive measures and parameter conversion for different parameterizations of the BMT distribution. Fit of the BMT distribution to non-censored data by maximum likelihood, moment matching, quantile matching, maximum goodness-of-fit, also known as minimum distance, maximum product of spacing, also called maximum spacing, and minimum quantile distance, which can also be called maximum quantile goodness-of-fit. Fit of univariate distributions for non-censored data using maximum product of spacing estimation and minimum quantile distance estimation is also included.
	"""
	
	cran = "BMT" 

	version("0.1.0.3", md5="54222894fe4217ba9a8ddbe6362fc412")

	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
