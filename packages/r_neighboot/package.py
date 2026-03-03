# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeighboot(RPackage):
	"""Neighborhood Bootstrap Method for RDS

	A bootstrap method for Respondent-Driven Sampling (RDS) that relies on the underlying structure of the RDS network to estimate uncertainty.
	"""
	
	cran = "Neighboot" 

	version("1.0.1", md5="1e7395d0cfe07a1b2eaa6a0147889657")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdstreeboot", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rds", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
