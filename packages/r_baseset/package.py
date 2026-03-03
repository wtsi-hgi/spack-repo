# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaseset(RPackage):
	"""Working with Sets the Tidy Way

	Implements a class and methods to work with sets,
    doing intersection, union, complementary sets, power sets, cartesian
    product and other set operations in a "tidy" way. These set operations
    are available for both classical sets and fuzzy sets. Import sets from
    several formats or from other several data structures.
	"""
	
	homepage = "https://github.com/ropensci/BaseSet"
	cran = "BaseSet" 

	version("0.9.0", md5="6c15aa4f04cc548d3dbb51858a57951c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
