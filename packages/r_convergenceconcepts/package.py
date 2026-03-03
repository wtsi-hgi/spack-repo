# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvergenceconcepts(RPackage):
	"""Seeing Convergence Concepts in Action

	This is a pedagogical package, designed to help students understanding convergence of
             random variables. It provides a way to investigate interactively various modes of
	     convergence (in probability, almost surely, in law and in mean) of a sequence of i.i.d.
	     random variables. Visualisation of simulated sample paths is possible through interactive
	     plots. The approach is illustrated by examples and exercises through the function
	     'investigate', as described in
	     Lafaye de Micheaux and Liquet (2009) <doi:10.1198/tas.2009.0032>.
	     The user can study his/her own sequences of random variables.
	"""
	
	cran = "ConvergenceConcepts" 

	version("1.2.3", md5="a122a2079f7e9d03c6cfb1c12a907fd9")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
