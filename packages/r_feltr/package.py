# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeltr(RPackage):
	"""Access the Felt API

	Upload, download, and edit internet maps with the Felt API 
    (<https://feltmaps.notion.site/Felt-Public-API-reference-c01e0e6b0d954a678c608131b894e8e1>). 
    Allows users to create new maps, edit existing maps, and extract data.
    Provides tools for working with layers, which represent geographic data, and elements,
    which are interactive annotations. Spatial data accessed from the API is 
    transformed to work with 'sf'.
	"""
	
	homepage = "https://github.com/christopherkenny/feltr"
	cran = "feltr" 

	version("0.0.4", md5="37416c7c0396c268134f2f63463921ca")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
