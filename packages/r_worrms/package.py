# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorrms(RPackage):
	"""World Register of Marine Species (WoRMS) Client

	Client for World Register of Marine Species
    (<https://www.marinespecies.org/>). Includes functions for each
    of the API methods, including searching for names by name, date and
    common names, searching using external identifiers, fetching
    synonyms, as well as fetching taxonomic children and
    taxonomic classification.
	"""
	
	homepage = "https://docs.ropensci.org/worrms/"
	cran = "worrms" 

	version("0.4.3", md5="4f95c3677fcb45baa23dbbae68c9a2cc")

	depends_on("r-crul@0.6:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
