# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanadamaps(RPackage):
	"""Maps of the Political and Administrative Divisions of Canada

	Terrestrial maps with simplified topologies for Census Divisions,
    Agricultural Regions, Economic Regions, Federal Electoral Divisions and
    Provinces.
	"""
	
	homepage = "https://github.com/pachadotdev/canadamaps/"
	cran = "canadamaps" 

	version("0.1", md5="176f2be539693a14a044901e49cd1b78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
