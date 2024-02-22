# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRangebuilder(RPackage):
	"""Occurrence Filtering, Geographic Standardization and Generation
of Species Range Polygons

	Provides tools for filtering occurrence records, generating alpha-hull-derived range polygons and mapping species distributions. 
	"""
	
	homepage = "https://github.com/ptitle/rangeBuilder"
	cran = "rangeBuilder" 

	version("2.1", md5="c61a10d670eae914e0d88ad0d48923ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-alphahull@2.5:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-rnaturalearth", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
