# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemify(RPackage):
	"""Processing and Transforming Relational Event History Data

	Efficiently processes relational event history data and transforms them into formats suitable for other packages. The primary objective of this package is to convert event history data into a format that integrates with the packages in 'remverse' and is compatible with various analytical tools (e.g., computing network statistics, estimating tie-oriented or actor-oriented social network models). Second, it can also transform the data into formats compatible with other packages out of 'remverse'. The package processes the data for two types of temporal social network models: tie-oriented modeling framework (Butts, C., 2008, <doi:10.1111/j.1467-9531.2008.00203.x>) and actor-oriented modeling framework (Stadtfeld, C., & Block, P., 2017, <doi:10.15195/v4.a14>). 
	"""
	
	homepage = "https://github.com/TilburgNetworkGroup/remify"
	cran = "remify" 

	version("3.2.5", md5="9820e667f88eca1faec879d951003680")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph@1.4.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
