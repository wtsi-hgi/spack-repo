# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTkcat(RPackage):
	"""Tailored Knowledge Catalog

	Facilitate the management of data from knowledge
   resources that are frequently used alone or together
   in research environments.
   In 'TKCat', knowledge resources are manipulated as modeled database (MDB)
   objects. These objects provide access to the data tables along with a general
   description of the resource and a detail data model documenting the
   tables, their fields and their relationships.
   These MDBs are then gathered in catalogs that can be easily
   explored an shared.
   Finally, 'TKCat' provides tools to easily subset, filter and combine MDBs and
   create new catalogs suited for specific needs.
	"""
	
	homepage = "https://patzaw.github.io/TKCat/"
	cran = "TKCat" 

	version("1.0.7", md5="f2abb700d6aea7e849e94bb4a6870ad2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-redamor@0.7:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-clickhousehttp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonvalidate@1.3.2:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
