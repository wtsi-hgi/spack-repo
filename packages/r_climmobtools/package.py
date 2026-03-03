# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimmobtools(RPackage):
	"""API Client for the 'ClimMob' Platform

	API client for 'ClimMob', an open source software for decentralized 
    large-N trials with the 'tricot' approach <https://climmob.net/>. 
    Developed by van Etten et al. (2019) <doi:10.1017/S0014479716000739>, it turns the 
    research paradigm on its head; instead of a few researchers designing complicated 
    trials to compare several technologies in search of the best solutions for the 
    target environment, it enables many participants to carry out reasonably simple 
    experiments that taken together can offer even more information. 'ClimMobTools' 
    enables project managers to deep explore and analyse their 'ClimMob' data in R.
	"""
	
	homepage = "https://agrdatasci.github.io/ClimMobTools/"
	cran = "ClimMobTools" 

	version("1.2", md5="0353c05209acf4fa4d5cd9ff9ff9636d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
