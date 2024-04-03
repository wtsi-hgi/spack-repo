# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMexhaz(RPackage):
	"""Mixed Effect Excess Hazard Models

	Fit flexible (excess) hazard regression models with the possibility of including non-proportional effects of covariables and of adding a random effect at the cluster level (corresponding to a shared frailty). A detailed description of the package functionalities is provided in Charvat and Belot (2021) <doi: 10.18637/jss.v098.i14>.
	"""
	
	cran = "mexhaz" 

	version("2.5", md5="96c860b9c1874a0134a8911fbf855a6c")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lamw", type=("build", "run"))
