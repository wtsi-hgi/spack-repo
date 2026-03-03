# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdl(RPackage):
	"""Interface and Tools for 'BDL' API

	Interface to Local Data Bank ('Bank Danych Lokalnych' - 'bdl') API 
    <https://api.stat.gov.pl/Home/BdlApi?lang=en> with set of useful tools like 
    quick plotting and map generating using data from bank. 
	"""
	
	homepage = "https://statisticspoland.github.io/R_Package_to_API_BDL/"
	cran = "bdl" 

	version("1.0.5", md5="d1b0d98b2b3e77dac85b63fb84291c93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tmaptools", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
