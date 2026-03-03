# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdagio(RPackage):
	"""Discrete and Global Optimization Routines

	
    The R package 'adagio' will provide methods and algorithms for
    (discrete) optimization, e.g. knapsack and subset sum procedures,
	derivative-free Nelder-Mead and Hooke-Jeeves minimization, and
	some (evolutionary) global optimization functions.
	"""
	
	cran = "adagio" 

	version("0.9.2", md5="233ef6554f85653593b9308f51525ffd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lpsolve@5.6.15:", type=("build", "run"))
