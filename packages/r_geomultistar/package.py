# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomultistar(RPackage):
	"""Multidimensional Queries Enriched with Geographic Data

	Multidimensional systems allow complex queries to be carried
    out in an easy way. The geographical dimension, together with the
    temporal dimension, plays a fundamental role in multidimensional
    systems. Through this package, vector geographic data layers can be
    associated to the attributes of geographic dimensions, so that the
    results of multidimensional queries can be obtained directly as vector
    layers.  The multidimensional structures on which we can define the
    queries can be created from a flat table or imported directly using
    functions from this package.
	"""
	
	homepage = "https://josesamos.github.io/geomultistar/"
	cran = "geomultistar" 

	version("1.2.1", md5="1fc2967f1c3fc70328eaea8829d4b2b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
