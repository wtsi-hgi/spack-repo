# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimbr(RPackage):
	"""Forest/Tree Data Frames

	Provides data frames for forest or tree data structures. You can 
    create forest data structures from data frames and process them based on 
    their hierarchies.
	"""
	
	homepage = "https://github.com/UchidaMizuki/timbr"
	cran = "timbr" 

	version("0.2.2", md5="cb198414b81f2f182fae3582fe1ebd93")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-vctrs@0.5.2:", type=("build", "run"))
