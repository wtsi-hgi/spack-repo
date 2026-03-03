# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimstrat(RPackage):
	"""Choosing the Sample Strategy

	Intended to assist in the choice of the sampling strategy to implement in a survey.
	"""
	
	cran = "optimStrat" 

	version("2.4", md5="63e449cc81d32219ed10ea1cbb18dcb7")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
