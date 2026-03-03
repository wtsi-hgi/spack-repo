# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivegp(RPackage):
	"""Gaussian Process Based Design and Analysis for the Active
Subspace Method

	The active subspace method is a sensitivity analysis technique that finds important linear combinations of input variables for a simulator. This package provides functions allowing estimation of the active subspace without gradient information using Gaussian processes as well as sequential experimental design tools to minimize the amount of data required to do so. Implements Wycoff et al. (2019) <arXiv:1907.11572>.
	"""
	
	cran = "activegp" 

	version("1.1.0", md5="c68a4ad0f433c7094f4274b038550534")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hetgp@1.1.1:", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
