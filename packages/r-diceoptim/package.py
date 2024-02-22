# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiceoptim(RPackage):
	"""Kriging-Based Optimization for Computer Experiments

	Efficient Global Optimization (EGO) algorithm as described in "Roustant et al. (2012)" <doi:10.18637/jss.v051.i01> and adaptations for problems with noise ("Picheny and Ginsbourger, 2012") <doi:10.1016/j.csda.2013.03.018>, parallel infill, and problems with constraints.
	"""
	
	homepage = "http://dice.emse.fr/"
	cran = "DiceOptim" 

	version("2.1.1", md5="77e4505ba094de9054c78e56841d7576")

	depends_on("r-dicekriging@1.2:", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-dicedesign", type=("build", "run"))
