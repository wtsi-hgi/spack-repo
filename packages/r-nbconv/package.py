# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbconv(RPackage):
	"""Evaluate Arbitrary Negative Binomial Convolutions

	Three distinct methods are implemented for evaluating the sums of arbitrary negative binomial distributions. These methods are: Furman's exact probability mass function (Furman (2007) <doi:10.1016/j.spl.2006.06.007>), saddlepoint approximation, and a method of moments approximation. Functions are provided to calculate the density function, the distribution function and the quantile function of the convolutions in question given said evaluation methods. Functions for generating random deviates from negative binomial convolutions and for directly calculating the mean, variance, skewness, and excess kurtosis of said convolutions are also provided.
	"""
	
	homepage = "https://github.com/gbedwell/nbconv"
	cran = "nbconv" 

	version("1.0.1", md5="1420ccc0a13d86bd9e314a0c09535bf7")

	depends_on("r-matrixstats", type=("build", "run"))
