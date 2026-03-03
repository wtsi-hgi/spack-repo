# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsland(RPackage):
	"""Stochastic Island Biogeography Theory Made Easy

	Develops stochastic models based on the Theory of Island
    Biogeography (TIB) of MacArthur and Wilson (1967) <doi:10.1023/A:1016393430551>
    and extensions. It implements methods to estimate colonization and
    extinction rates (including environmental variables) given presence-absence
    data, simulates community assembly, and performs model selection.
	"""
	
	cran = "island" 

	version("0.2.10", md5="6584a920b3266bf6f16ef328d8cdd7c4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
