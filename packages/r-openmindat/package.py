# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenmindat(RPackage):
	"""Quickly Retrieve Datasets from the 'mindat.org' API

	'Mindat' ('mindat.org') is one of the world's most widely used databases of mineral species and their distribution. Many scientists in mineralogy, geochemistry, petrology, and other Earth and planetary disciplines have been using the 'Mindat' data. Still, an open data service and the machine interface have never been fully established. To meet the overwhelming data needs, the 'Mindat' team has built an API (<https://api.mindat.org/schema/redoc/>) for data access.'OpenMindat' R package provides valuable functions to bridge the data highway, connecting users' data requirements to the 'Mindat' API server and assist with retrieval and initial processing to improve efficiency further and lower the barrier of data query and access to scientists. 'OpenMindat' provides friendly and extensible data retrieval functions, including the subjects of geomaterials (e.g., rocks, minerals, synonyms, variety, mixture, and commodity), localities, and the IMA (International Mineralogical Association)-approved mineral list. 'OpenMindat' R package will accelerate the process of data-intensive studies in mineral informatics and lead to more scientific discoveries.
	"""
	
	homepage = "https://github.com/quexiang/OpenMindat"
	cran = "OpenMindat" 

	version("1.0.0", md5="c3a6a062ed6412832df1a5054b0b818e")

	depends_on("r-httr@1.4.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.4:", type=("build", "run"))
	depends_on("r-readxl@1.4.3:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
