# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdfquantreg(RPackage):
	"""Quantile Regression for Random Variables on the Unit Interval

	Employs a two-parameter family of
    distributions for modelling random variables on the (0, 1) interval by
    applying the cumulative distribution function (cdf) of one parent
    distribution to the quantile function of another.
	"""
	
	cran = "cdfquantreg" 

	version("1.3.1-2", md5="95d298ae526c39002b6bf81e97bb0b6a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma@2.3:", type=("build", "run"))
	depends_on("r-formula@1.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
