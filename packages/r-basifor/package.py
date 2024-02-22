# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasifor(RPackage):
	"""Retrieval and Processing of the Spanish National Forest
Inventory

	Data sets of the Spanish National Forest Inventory <https://www.miteco.gob.es/es/biodiversidad/servicios/banco-datos-naturaleza/informacion-disponible/> are processed to compute tree metrics and statistics. Function metrics2Vol() controls most of the routines.
	"""
	
	cran = "basifoR" 

	version("0.4", md5="d51b86de82d1d6d681d498c5a906391f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-measurements", type=("build", "run"))
