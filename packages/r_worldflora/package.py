# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorldflora(RPackage):
	"""Standardize Plant Names According to World Flora Online
Taxonomic Backbone

	World Flora Online is an online flora of all known plants, available from <https://www.worldfloraonline.org/>. Methods are provided of matching a list of plant names (scientific names, taxonomic names, botanical names) against a static copy of the World Flora Online Taxonomic Backbone data that can be downloaded from the World Flora Online website. The World Flora Online Taxonomic Backbone is an updated version of The Plant List (<http://www.theplantlist.org/>), a working list of plant names that has become static since 2013.
	"""
	
	cran = "WorldFlora" 

	version("1.14-2", md5="8c77fecc9b7988bd9985ab3718826ea4")
	version("1.14-1", md5="2affaee62151add6fa0b25fe21856203")

	depends_on("r@3.5:", type=("build", "run"))
