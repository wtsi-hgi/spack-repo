# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCccp(RPackage):
	"""Cone Constrained Convex Problems

	Routines for solving convex optimization problems with cone constraints by means of interior-point methods. The implemented algorithms are partially ported from CVXOPT, a Python module for convex optimization (see <https://cvxopt.org> for more information). 
	"""
	
	cran = "cccp" 

	version("0.3-1", md5="9d924a1a49c1df927fa8fbdf49a6c8d5")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
