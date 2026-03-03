# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemds(RPackage):
	"""Structural Equation Multidimensional Scaling

	Fits a structural equation multidimensional scaling (SEMDS) model for asymmetric and three-way input dissimilarities. It assumes that the dissimilarities are measured with errors. The latent dissimilarities are estimated as factor scores within an SEM framework while the objects are represented in a low-dimensional space as in MDS. 
	"""
	
	cran = "semds" 

	version("0.9-6", md5="db04737c58a2783bb035851c301dca7f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
