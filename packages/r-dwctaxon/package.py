# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwctaxon(RPackage):
	"""Edit and Validate Darwin Core Taxon Data

	Edit and validate taxonomic data in compliance with Darwin Core
    standards (Darwin Core 'Taxon' class <https://dwc.tdwg.org/terms/#taxon>).
	"""
	
	homepage = "https://docs.ropensci.org/dwctaxon/"
	cran = "dwctaxon" 

	version("2.0.3", md5="8299ad66cb7006e494ec88f2444f01c4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
