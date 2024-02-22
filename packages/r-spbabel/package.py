# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpbabel(RPackage):
	"""Convert Spatial Data Using Tidy Tables

	Tools to convert from specific formats to more general forms of 
    spatial data. Using tables to store the actual entities present in spatial
    data provides flexibility, and the functions here deliberately 
    minimize the level of interpretation applied, leaving that for specific 
    applications. Includes support for simple features,  round-trip for 'Spatial' classes and long-form 
    tables, analogous to 'ggplot2::fortify'. There is also a more 'normal form' representation
    that decomposes simple features and their kin to tables of objects, parts, and unique coordinates. 
	"""
	
	homepage = "https://mdsumner.github.io/spbabel/"
	cran = "spbabel" 

	version("0.6.0", md5="df4e821049b1c287931ca6575216a911")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
