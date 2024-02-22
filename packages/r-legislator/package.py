# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLegislator(RPackage):
	"""Interface to the Comparative Legislators Database

	Facilitates access to the Comparative Legislators Database (CLD). The CLD includes political, sociodemographic, career, online presence, public attention, and visual information for over 67,000 contemporary and historical politicians from 16 countries.
	"""
	
	homepage = "https://github.com/saschagobel/legislatoR"
	cran = "legislatoR" 

	version("1.1.0", md5="fce40247f1bfdde606662a04409686f9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl@3:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
