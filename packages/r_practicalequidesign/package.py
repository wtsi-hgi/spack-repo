# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPracticalequidesign(RPackage):
	"""Design of Practical Equivalence Trials

	Sample size calculations for practical equivalence trial design with a time to event endpoint. 
	"""
	
	cran = "PracticalEquiDesign" 

	version("0.0.3", md5="67673c7e0f2d1b55175c03d95e691880")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-temporal", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
