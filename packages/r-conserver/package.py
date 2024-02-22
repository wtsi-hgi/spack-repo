# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConserver(RPackage):
	"""Identifying Conservation Prioritization Methods Based on Data
Availability

	Helping biologists to choose the most suitable approach to link their research to conservation. After answering few questions on the data available, geographic and taxonomic scope, 'conserveR' ranks existing methods for conservation prioritization and systematic conservation planning by suitability. The methods data base of 'conserveR' contains 133 methods for conservation prioritization based on a systematic review of > 12,000 scientific publications from the fields of spatial conservation prioritization, systematic conservation planning, biogeography and ecology.
	"""
	
	homepage = "https://github.com/azizka/conserveR"
	cran = "conserveR" 

	version("1.0.4", md5="174e6556609ac92b0b4e205420a09066")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
