# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMipp(RPackage):
	"""Misclassification Penalized Posterior Classification

	This package finds optimal sets of genes that seperate samples into two or more classes.
	"""
	
	homepage = "http://www.healthsystem.virginia.edu/internet/hes/biostat/bioinformatics/"
	bioc = "MiPP"

	version("1.80.0", commit="39b272558073d9f04aab4e0f9c9c04952d54dd01")
	version("1.74.0", commit="6d11cd847ae8850b382ca3f116acfb54da478ff9")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
