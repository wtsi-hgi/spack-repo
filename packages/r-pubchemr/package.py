# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubchemr(RPackage):
	"""Interface to the 'PubChem' Database for Chemical Data Retrieval

	Provides an interface to the 'PubChem' database via the PUG REST <https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest> and 
            PUG View <https://pubchem.ncbi.nlm.nih.gov/docs/pug-view> services. This package allows users to automatically 
            access chemical and biological data from 'PubChem', including compounds, substances, assays, and various other data types. 
            Functions are available to retrieve data in different formats, perform searches, and access detailed annotations.
	"""
	
	cran = "PubChemR" 

	version("1.2", md5="73873caf602f8b897954a94a6163027a")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
