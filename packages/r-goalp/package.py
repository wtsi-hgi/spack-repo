# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoalp(RPackage):
	"""Weighted and Lexicographic Goal Programming Interface

	Solves goal programming problems of the weighted and  
    lexicographic type, as well as combinations of the two, as described 
    by Ignizio (1983) <doi:10.1016/0305-0548(83)90003-5>. Allows for 
    a simple human-readable input describing the problem as a series 
    of equations. Relies on the 'lpSolve' package to solve the underlying 
    linear optimisation problem.
	"""
	
	cran = "goalp" 

	version("0.3.1", md5="1565a491f289abc59445f99dfbca16b6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
