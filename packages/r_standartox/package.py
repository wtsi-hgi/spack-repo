# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStandartox(RPackage):
	"""Ecotoxicological Information from the Standartox Database

	The <http://standartox.uni-landau.de> database offers cleaned,
    harmonized and aggregated ecotoxicological test data, which can
    be used for assessing effects and risks of chemical concentrations
    found in the environment.
	"""
	
	homepage = "https://github.com/andschar/standartox"
	cran = "standartox" 

	version("0.0.2", md5="b20e02adcab0ac591163d1f7081d80e3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-fst@0.9.4:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
