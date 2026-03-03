# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoll(RPackage):
	"""Rolling and Expanding Statistics

	Fast and efficient computation of rolling and expanding statistics for time-series data.
	"""
	
	homepage = "https://github.com/jjf234/roll"
	cran = "roll" 

	version("1.1.6", md5="340ef60b1e5103555a81b309fe81bed6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
