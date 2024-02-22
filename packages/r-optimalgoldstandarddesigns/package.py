# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalgoldstandarddesigns(RPackage):
	"""Design Parameter Optimization for Gold-Standard Non-Inferiority
Trials

	Methods to calculate optimal design parameters
    for one- and two-stage three-arm group-sequential gold-standard
    non-inferiority trial designs
    with or without binding or nonbinding futility boundaries,
    as described in Meis et al. (2023) <doi:10.1002/sim.9630>.
	"""
	
	homepage = "https://github.com/jan-imbi/OptimalGoldstandardDesigns"
	cran = "OptimalGoldstandardDesigns" 

	version("1.0.1", md5="99e669d1e508a948cc2f6445cc51f48a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
