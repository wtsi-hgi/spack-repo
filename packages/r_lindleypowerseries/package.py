# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLindleypowerseries(RPackage):
	"""Lindley Power Series Distribution

	Computes the probability density function, the cumulative distribution function, the hazard rate function, the quantile function and random generation for Lindley Power Series distributions, see Nadarajah and Si (2018) <doi:10.1007/s13171-018-0150-x>.
	"""
	
	cran = "LindleyPowerSeries" 

	version("1.0.1", md5="533a9be7346c818443282703c1078338")

	depends_on("r-lamw@1.3:", type=("build", "run"))
