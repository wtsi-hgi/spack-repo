# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangeranger(RPackage):
	"""Change Metrics for Species Geographic Ranges

	Facilitates workflows to reproducibly transform estimates of
    species’ distributions into metrics relevant for conservation. For
    example, combining predictions from species distribution models with other
    maps of environmental data to characterize the proportion of a species’
    range that is under protection, calculating metrics used under the
    International Union for Conservation of Nature (IUCN) Criteria A and B
    guidelines (Area of Occupancy and Extent of Occurrence), and calculating
    more general metrics such as taxonomic and phylogenetic diversity, as well
    as endemism. Also facilitates temporal comparisons among biodiversity
    metrics to inform efforts towards complementarity and consideration of
    future scenarios in conservation decisions. 'changeRangeR' also provides
    tools to determine the effects of modeling decisions through sensitivity
    tests.
	"""
	
	cran = "changeRangeR" 

	version("1.1.0", md5="f3980049dfc5cecd96519dd88cad4b28")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rangemodelmetadata", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
