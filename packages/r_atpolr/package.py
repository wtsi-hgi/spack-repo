# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtpolr(RPackage):
	"""ATPOL Grid Implementation

	ATPOL is a rectangular grid system used for botanical studies in Poland. The ATPOL grid was developed in Institute of Botany, Jagiellonian University, Krakow, Poland in '70. Since then it is widely used to represent distribution of plants in Poland. 
    'atpolR' provides functions to translate geographic coordinates to the grid and vice versa. It also allows to create a choreograph map.
	"""
	
	homepage = "https://github.com/gsapijaszko/atpolR"
	cran = "atpolR" 

	version("0.1.1", md5="933ed76ccb2f6439bbd712012ff0be58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
