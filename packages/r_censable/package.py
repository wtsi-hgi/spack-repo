# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensable(RPackage):
	"""Making Census Data More Usable

	Creates a common framework for organizing, naming, and gathering 
    population, age, race, and ethnicity data from the Census Bureau. Accesses 
    the API <https://www.census.gov/data/developers/data-sets.html>. Provides 
    tools for adding information to existing data to line up with Census data.
	"""
	
	homepage = "https://christophertkenny.com/censable/"
	cran = "censable" 

	version("0.0.5", md5="71345eff43ec356d826f7f0ba6c3be7a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1.0.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-censusapi", type=("build", "run"))
	depends_on("r-tinytiger", type=("build", "run"))
