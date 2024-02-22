# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcdata(RPackage):
	"""Search and Retrieve Data from the BC Data Catalogue

	Search, query, and download tabular and
    'geospatial' data from the British Columbia Data Catalogue
    (<https://catalogue.data.gov.bc.ca/>).  Search catalogue data records
    based on keywords, data licence, sector, data format, and B.C.
    government organization. View metadata directly in R, download many
    data formats, and query 'geospatial' data available via the B.C.
    government Web Feature Service ('WFS') using 'dplyr' syntax.
	"""
	
	homepage = "https://bcgov.github.io/bcdata/"
	cran = "bcdata" 

	version("0.4.1", md5="fbdce8b3dc2fd7822f615d975b46e82c")

	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-crul@1.1:", type=("build", "run"))
	depends_on("r-dbplyr@2.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tibble@3.1:", type=("build", "run"))
	depends_on("r-glue@1.6:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-leaflet@2.1:", type=("build", "run"))
	depends_on("r-leaflet-extras@1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-readr@2.1:", type=("build", "run"))
	depends_on("r-readxl@1.4:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-xml2@1.3:", type=("build", "run"))
