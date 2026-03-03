# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2openbugs(RPackage):
	"""Running OpenBUGS from R

	Using this package,
 it is possible to call a BUGS model, summarize inferences and
 convergence in a table and graph, and save the simulations in arrays for easy access
 in R. 
	"""
	
	cran = "R2OpenBUGS" 

	version("3.2-3.2.1", md5="ce759b2d1c9f5ffc152dd6106d04533c")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-coda@0.11.0:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
