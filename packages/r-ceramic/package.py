# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeramic(RPackage):
	"""Download Online Imagery Tiles

	Download imagery tiles to a standard cache and load the data into raster objects. 
 Facilities for 'AWS' terrain <https://registry.opendata.aws/terrain-tiles/> terrain and 'Mapbox' 
 <https://www.mapbox.com/> servers are provided. 
	"""
	
	homepage = "https://hypertidy.github.io/ceramic/"
	cran = "ceramic" 

	version("0.9.5", md5="74c86ca99efe7c6d04ec662b2be9b063")
	version("0.9.0", md5="c7682b522e59bda855aad7d3935e6c1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs@1.3:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-slippymath@0.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crsmeta", type=("build", "run"))
	depends_on("r-vapour", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
