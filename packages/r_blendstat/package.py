# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlendstat(RPackage):
	"""Joint Analysis of Experiments with Mixtures and Random Effects

	Performs a joint analysis of experiments with mixtures and random effects, taking on a process variable represented by a covariable.
	"""
	
	cran = "Blendstat" 

	version("1.0.4", md5="767dc4e8c12e6b14a78904478b4c1364")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
