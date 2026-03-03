# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpboost(RPackage):
	"""Treatment Allocation in Clinical Trials by the Maximal Procedure

	Performs treatment allocation in two-arm clinical trials by the maximal procedure described by Berger et al. (2003) <doi:10.1002/sim.1538>. To that end, the algorithm provided by Salama et al. (2008) <doi:10.1002/sim.3014> is implemented.
	"""
	
	cran = "MPBoost" 

	version("0.1-6", md5="2994fb6802f7eb35f269c0885975f4fb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
