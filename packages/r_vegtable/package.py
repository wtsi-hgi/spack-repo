# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegtable(RPackage):
	"""Handling Vegetation Data Sets

	Import and handling data from vegetation-plot databases, especially
    data stored in 'Turboveg 2' (<https://www.synbiosys.alterra.nl/turboveg/>).
    Also import/export routines for exchange of data with 'Juice'
    (<https://www.sci.muni.cz/botany/juice/>) are implemented.
	"""
	
	homepage = "https://github.com/kamapu/vegtable"
	cran = "vegtable" 

	version("0.1.8", md5="ed68d50b199fc060b124e237b1c8aa46")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-taxlist@0.2.4:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-vegdata", type=("build", "run"))
