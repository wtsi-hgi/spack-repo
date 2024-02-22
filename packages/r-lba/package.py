# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLba(RPackage):
	"""Latent Budget Analysis for Compositional Data

	Latent budget analysis is a method for the analysis of a two-way
    contingency table with an exploratory variable and a response variable. It is
    specially designed for compositional data.
	"""
	
	homepage = "https://github.com/ivanalaman/lba"
	cran = "lba" 

	version("2.4.52", md5="2ea12f2932479bd7e2df45f9e70566a0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
