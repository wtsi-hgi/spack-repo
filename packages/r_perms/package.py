# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerms(RPackage):
	"""Fast Permutation Computation

	Implements the algorithm of Christensen (2023) <doi:10.1214/22-BA1353> for estimating marginal likelihoods via permutation counting. 
	"""
	
	cran = "perms" 

	version("1.13", md5="4012938e992e8b27366987264557199c")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
