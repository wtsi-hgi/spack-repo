# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepons2r(RPackage):
	"""Read, Plot and Analyse Output from the DEPONS Model

	Methods for analyzing population dynamics and movement tracks simulated using the DEPONS model <https://www.depons.eu> (v.3.0), for manipulating input raster files, shipping routes and for analyzing sound propagated from ships.
	"""
	
	cran = "DEPONS2R" 

	version("1.2.2", md5="1d470e5eaf32c2c65acbea0c9e01c8bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
