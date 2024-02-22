# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsdinterface(RPackage):
	"""Interface Tools for LSD Simulation Results Files

	Interfaces R with LSD simulation models. Reads object-oriented data in results files (.res[.gz]) produced by LSD and creates appropriate multi-dimensional arrays in R. Supports multiple core parallel threads of multi-file data reading for increased performance. Also provides functions to extract basic information and statistics from data files. LSD (Laboratory for Simulation Development) is free software developed by Marco Valente and Marcelo C. Pereira (documentation and downloads available at <https://www.labsimdev.org/>).
	"""
	
	cran = "LSDinterface" 

	version("1.2.1", md5="8950d0b7e8708fd3b744f53d04fd3b44")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-tsdist", type=("build", "run"))
