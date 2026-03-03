# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPotions(RPackage):
	"""Easy Options Management

	Store and retrieve data from options() using syntax derived from
    the 'here' package. 'potions' makes it straightforward to update and 
    retrieve options, either in the workspace or during package development, 
    without overwriting global options.
	"""
	
	homepage = "https://potions.ala.org.au"
	cran = "potions" 

	version("0.2.0", md5="dcdc909419bb697774d3e858eafbfab2")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rrapply", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
