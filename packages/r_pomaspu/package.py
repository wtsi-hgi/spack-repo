# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomaspu(RPackage):
	"""Adaptive Association Tests for Multiple Phenotypes using
Proportional Odds Model (POM-aSPU)

	POM-aSPU test evaluates an association between an ordinal response and multiple phenotypes, for details see Kim and Pan (2017) <DOI:10.1002/gepi.22033>.
	"""
	
	cran = "POMaSPU" 

	version("1.0.0", md5="0f475e7b77922ede9a0ad231e5619eb4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
