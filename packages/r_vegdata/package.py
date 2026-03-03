# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegdata(RPackage):
	"""Access Vegetation Databases and Treat Taxonomy

	Handling of vegetation data from different sources (
	Turboveg 2.0 <https://www.synbiosys.alterra.nl/turboveg/>; 
	the German national repository <https://www.vegetweb.de> and others. 
    Taxonomic harmonization (given appropriate taxonomic lists,
    e.g. the German taxonomic standard list "GermanSL", <https://germansl.infinitenature.org>).
	"""
	
	homepage = "https://germansl.infinitenature.org"
	cran = "vegdata" 

	version("0.9.12", md5="a6151e4bfe0736a8c3e301cb79603921")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-curl@2.4:", type=("build", "run"))
	depends_on("r-dbi@0.6.1:", type=("build", "run"))
	depends_on("r-rsqlite@1.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-dbplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-hoardr@0.1:", type=("build", "run"))
	depends_on("r-indicspecies", type=("build", "run"))
	depends_on("r-xml2@1.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
