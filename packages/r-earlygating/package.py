# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarlygating(RPackage):
	"""Properties of Bayesian Early Gating Designs

	Computes the most important properties of four 'Bayesian' early gating 
             designs (two single arm and two randomized controlled designs), such 
             as minimum required number of successes in the experimental group to 
             make a GO decision, operating characteristics and average operating 
             characteristics with respect to the sample size. 
             These might aid in deciding what design to use for the early phase trial.
	"""
	
	cran = "earlygating" 

	version("1.1", md5="16b4c669f311195f828a93d1a0e6f080")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
