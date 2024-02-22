# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsi(RPackage):
	"""Efficiently Retrieve and Process Satellite Imagery

	Downloads spatial data from spatiotemporal asset catalogs 
    ('STAC'), computes standard spectral indices from the Awesome Spectral 
    Indices project (Montero et al. (2023) <doi:10.1038/s41597-023-02096-0>) 
    against raster data, and glues the outputs together into predictor bricks. 
    Methods focus on interoperability with the broader spatial ecosystem; 
    function arguments and outputs use classes from 'sf' and 'terra', and data 
    downloading functions support complex 'CQL2' queries using 'rstac'.
	"""
	
	homepage = "https://github.com/Permian-Global-Research/rsi"
	cran = "rsi" 

	version("0.1.2", md5="3ac2cca892d56b8b29964c39984d36a0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-proceduralnames", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstac", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
