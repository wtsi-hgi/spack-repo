# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiftree(RPackage):
	"""Item Focussed Trees for the Identification of Items in
Differential Item Functioning

	Item focussed recursive partitioning for simultaneous selection of items and variables that induce Differential Item Functioning (DIF) in dichotomous or polytomous items. 
	"""
	
	cran = "DIFtree" 

	version("3.1.6", md5="7106a1972d4a93986e9732ce078a3771")

	depends_on("r-penalized", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
