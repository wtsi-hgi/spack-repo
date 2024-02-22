# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridpattern(RPackage):
	"""'grid' Pattern Grobs

	Provides 'grid' grobs that fill in a user-defined area with various patterns.  Includes enhanced versions of the geometric and image-based patterns originally contained in the 'ggpattern' package as well as original 'pch', 'polygon_tiling', 'regular_polygon', 'rose', 'text', 'wave', and 'weave' patterns plus support for custom user-defined patterns.
	"""
	
	homepage = "https://trevorldavis.com/R/gridpattern/"
	cran = "gridpattern" 

	version("1.1.1", md5="08dd2def166d2ccf589fa83fd1bf9b0c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
