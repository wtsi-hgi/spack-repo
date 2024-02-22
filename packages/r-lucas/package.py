# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLucas(RPackage):
	"""Package to Download and Create the DB of LUCAS Data Harmonized

	Reproduces the harmonized DB of the ESTAT survey of the same name. The survey data is served as separate spreadsheets with noticeable differences in the collected attributes. The tool here presented carries out a series of instructions that harmonize the attributes in terms of name, meaning, and occurrence, while also introducing a series of new variables, instrumental to adding value to the product. Outputs include one harmonized table with all the years, and three separate geometries, corresponding to the theoretical point, the gps location where the measurement was made and the 250m east-facing transect.
	"""
	
	cran = "lucas" 

	version("1.0", md5="0b862e23e45d97de83f88bea3a339e37")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-rpostgis", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
