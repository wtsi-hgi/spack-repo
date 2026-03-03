# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMolhd(RPackage):
	"""Multiple Objective Latin Hypercube Design

	Generate the optimal maximin distance, minimax distance (only for low dimensions), and maximum projection designs within the class of Latin hypercube designs efficiently for computer experiments. Generate Pareto front optimal designs for each two of the three criteria and all the three criteria within the class of Latin hypercube designs efficiently. Provide criterion computing functions. References of this package can be found in Morris, M. D. and Mitchell, T. J. (1995) <doi:10.1016/0378-3758(94)00035-T>, Lu Lu and Christine M. Anderson-CookTimothy J. Robinson (2011) <doi:10.1198/Tech.2011.10087>, Joseph, V. R., Gul, E., and Ba, S. (2015) <doi:10.1093/biomet/asv002>.
	"""
	
	cran = "MOLHD" 

	version("0.2", md5="0ec921d70b68b3fbe851fdedef3570c8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
