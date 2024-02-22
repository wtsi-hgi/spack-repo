# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsmap(RPackage):
	"""US Maps Including Alaska and Hawaii

	Obtain United States map data frames of varying region types (e.g. county,
    state). The map data frames include Alaska and Hawaii conveniently placed to the
    bottom left, as they appear in most maps of the US. Convenience functions for plotting
    choropleths, visualizing spatial data, and working with FIPS codes are also provided.
	"""
	
	homepage = "https://usmap.dev"
	cran = "usmap" 

	version("0.7.0", md5="190c74e83b6013bb9b102fe2de2fe89b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-usmapdata@0.2:", type=("build", "run"))
