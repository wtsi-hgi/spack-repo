# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDprop(RPackage):
	"""Computation of Some Important Distributional Properties

	Generally, most of the packages specify the probability density function, cumulative distribution function, quantile function, and random numbers generation of the probability distributions. The present package allows to compute some important distributional properties, including the first four ordinary and central moments, Pearson's coefficient of skewness and kurtosis, the mean and variance, coefficient of variation, median, and quartile deviation at some parametric values of several well-known and extensively used probability distributions.
	"""
	
	cran = "dprop" 

	version("0.1.0", md5="4be7acf896b5180fa6db49fc7db96deb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-vares", type=("build", "run"))
