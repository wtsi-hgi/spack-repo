# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaddison(RPackage):
	"""The Maddison Project Database

	Contains the Maddison Project 2018 database, which provides 
    estimates of GDP per capita for all countries in the world between AD 1 and
    2016. See <https://www.rug.nl/ggdc/historicaldevelopment/maddison/> for more information.
	"""
	
	homepage = "https://www.rug.nl/ggdc/historicaldevelopment/maddison/"
	cran = "maddison" 

	version("0.2", md5="e954f38ef16c766b6bbcb3f5679f96e4")

	depends_on("r@3.5:", type=("build", "run"))
