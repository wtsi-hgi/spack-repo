# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcgen(RPackage):
	"""Reconstruction of Causal Networks for Data with Random Genetic
Effects

	Implements the pcgen algorithm, which is a modified version of the standard pc-algorithm,
             with specific conditional independence tests and modified orientation rules. pcgen extends 
			 the approach of Valente et al. (2010) <doi:10.1534/genetics.109.112979> with reconstruction of 
			 direct genetic effects.
	"""
	
	cran = "pcgen" 

	version("0.2.0", md5="7ad46c70213006ec76293e2b42b2272d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-sommer", type=("build", "run"))
	depends_on("r-ggm", type=("build", "run"))
