# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBraqca(RPackage):
	"""Bootstrapped Robustness Assessment for Qualitative Comparative
Analysis

	Test the robustness of a user's Qualitative Comparative Analysis
    solutions to randomness, using the bootstrapped assessment: baQCA(). This
    package also includes a function that provides recommendations for improving
    solutions to reach typical significance levels: brQCA(). Data included 
    come from McVeigh et al. (2014) <doi:10.1177/0003122414534065>.
	"""
	
	cran = "braQCA" 

	version("1.2.1.29", md5="5432e1302db01ac6bdd2be7e3aec95d2")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-qca", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
