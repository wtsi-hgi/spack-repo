# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrisonbrief(RPackage):
	"""Downloads and Parses World Prison Brief Data

	Download, parses and tidies information from the World Prison Brief project <http://www.prisonstudies.org/>. 
	"""
	
	homepage = "https://danilofreire.github.io/prisonbrief/"
	cran = "prisonbrief" 

	version("0.1.2", md5="1784bc81ddee0d61ec03d09975421f0e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sf@0.6:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-passport@0.1.1:", type=("build", "run"))
	depends_on("r-rnaturalearth@0.1:", type=("build", "run"))
	depends_on("r-rnaturalearthdata@0.1:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tibble@1.3.3:", type=("build", "run"))
	depends_on("r-tidyr@0.6.3:", type=("build", "run"))
	depends_on("r-xml2@1.1.1:", type=("build", "run"))
