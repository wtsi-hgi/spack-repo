# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcoe(RPackage):
	"""Creates New Folders and Loads Standard Practices for Monterey
County Office of Education

	Basic Setup for Projects in R for Monterey County Office of Education. It contains functions often used in the analysis of education data in the county office including seeing if an item is not in a list, rounding in the manner the general public expects, including logos for districts, switching between district names and their county-district-school codes, accessing the local 'SQL' table and making thematically consistent graphs.
	"""
	
	homepage = "https://github.com/dobrowski/MCOE"
	cran = "MCOE" 

	version("0.4.0", md5="f81ccd7a0a6a1371a43aea674d61fd44")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-googlesheets4", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
