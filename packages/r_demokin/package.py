# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemokin(RPackage):
	"""Estimate Population Kin Distribution

	Estimate population kin counts and its distribution by type, age and sex.
    The package implements one-sex and two-sex framework for studying living-death availability,
    with time varying rates or not, and multi-stage model.
	"""
	
	homepage = "https://github.com/IvanWilli/DemoKin"
	cran = "DemoKin" 

	version("1.0.3", md5="560e5d85f517ded40b5cfd3bc64d47ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
