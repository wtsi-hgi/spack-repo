# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpocc(RPackage):
	"""Interface to Species Occurrence Data Sources

	A programmatic interface to many species occurrence data sources,
    including Global Biodiversity Information Facility ('GBIF'), 'iNaturalist',
    'eBird', Integrated Digitized 'Biocollections' ('iDigBio'), 'VertNet', 
    Ocean 'Biogeographic' Information System ('OBIS'), and 
    Atlas of Living Australia ('ALA'). Includes functionality for retrieving
    species occurrence data, and combining those data.
	"""
	
	homepage = "https://github.com/ropensci/spocc"
	cran = "spocc" 

	version("1.2.3", md5="13a792f7de7abd3e70545a7399618865")

	depends_on("r-rgbif", type=("build", "run"))
	depends_on("r-rebird", type=("build", "run"))
	depends_on("r-rvertnet", type=("build", "run"))
	depends_on("r-ridigbio", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
	depends_on("r-s2", type=("build", "run"))
