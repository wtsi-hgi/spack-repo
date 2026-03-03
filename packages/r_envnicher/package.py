# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvnicher(RPackage):
	"""Niche Estimation

	A plot overlying the niche of multiple species is obtained: 1) to determine the niche conditions which favor a higher species richness, 2) to create a box plot with the range of environmental variables of the species, 3) to obtain a list of species in an area of the niche selected by the user and, 4) to estimate niche overlap among the species.
	"""
	
	cran = "EnvNicheR" 

	version("1.5", md5="cad486063648c62e7f4daa195b5ca3f2")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-idpmisc", type=("build", "run"))
