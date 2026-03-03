# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRodd(RPackage):
	"""Optimal Discriminating Designs

	A collection of functions for numerical construction of optimal discriminating designs. At the current moment T-optimal designs (which maximize the lower bound for the power of F-test for regression model discrimination), KL-optimal designs (for lognormal errors) and their robust analogues can be calculated with the package.  
	"""
	
	cran = "rodd" 

	version("0.2-1", md5="0c7b2a739c27d90eb1e563b420cc82d6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
