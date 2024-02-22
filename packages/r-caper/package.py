# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaper(RPackage):
	"""Comparative Analyses of Phylogenetics and Evolution in R

	Functions for performing phylogenetic comparative analyses.
	"""
	
	cran = "caper" 

	version("1.0.3", md5="8220e536ab9df155146b097cc25cac35")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape@3.0.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
