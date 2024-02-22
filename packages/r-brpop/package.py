# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrpop(RPackage):
	"""Brazilian Population Estimatives

	Datasets with yearly (2000 to 2021) Brazilian population estimates from DataSUS/Brazilian Health Ministry, aggregated by state, municipality, sex, and age groups. The data in this package is manually downloaded from the DataSUS website and converted to tibbles.
	"""
	
	homepage = "https://rfsaldanha.github.io/brpop/"
	cran = "brpop" 

	version("0.3.0", md5="46f175b1805322266604b8040325c953")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-multidplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
