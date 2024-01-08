# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RAlabama(RPackage):
	"""Constrained Nonlinear Optimization

	Augmented Lagrangian Adaptive Barrier Minimization
        Algorithm for optimizing smooth nonlinear objective functions
        with constraints. Linear or nonlinear equality and inequality
        constraints are allowed.
	"""
	
	cran = "alabama" 

	version("2023.1.0", md5="c5c8ed8a90efc7e142140f30237f4de6")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))

