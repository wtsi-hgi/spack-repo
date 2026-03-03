# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoadoi(RPackage):
	"""Find Free Versions of Scholarly Publications via Unpaywall

	This web client interfaces Unpaywall <https://unpaywall.org/products/api>, formerly
    oaDOI, a service finding free full-texts of academic papers by linking DOIs with 
    open access journals and repositories. It provides unified access to various data sources 
    for open access full-text links including Crossref and the Directory of Open Access 
    Journals (DOAJ). API usage is free and no registration is required.
	"""
	
	homepage = "https://docs.ropensci.org/roadoi/"
	cran = "roadoi" 

	version("0.7.2", md5="22d6ab19653667a56f82fede5bb359a6")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny@1.0.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
