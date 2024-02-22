# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElectionsbr(RPackage):
	"""R Functions to Download and Clean Brazilian Electoral Data

	Offers a set of functions to easily download and clean 
    Brazilian electoral data from the Superior Electoral Court website. 
    Among others, the package retrieves data on local and
    federal elections for all positions (city councilor, mayor, state deputy,
    federal deputy, governor, and president) aggregated by
    state, city, and electoral zones. 
	"""
	
	homepage = "http://electionsbr.com/"
	cran = "electionsBR" 

	version("0.4.0", md5="17c12745c613c409b25dd5696833759b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-haven@1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
