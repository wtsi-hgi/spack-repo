# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDips(RPackage):
	"""Directional Penalties for Optimal Matching in Observational
Studies

	Improves the balance of optimal matching with near-fine balance by giving penalties on the unbalanced covariates with the unbalanced directions. Many directional penalties can also be viewed as Lagrange multipliers, pushing a matched sample in the direction of satisfying a linear constraint that would not be satisfied without penalization.
    Yu and Rosenbaum (2019) <doi:10.1111/biom.13098>. 
	"""
	
	cran = "DiPs" 

	version("0.6.4", md5="0233ae26a36bb236d0e909ebcfe8b6cf")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rlemon", type=("build", "run"))
