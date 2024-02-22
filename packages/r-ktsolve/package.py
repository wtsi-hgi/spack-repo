# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKtsolve(RPackage):
	"""Configurable Function for Solving Families of Nonlinear
Equations

	This is designed for use with an arbitrary set of equations with
 an arbitrary set of unknowns.
 The user selects "fixed" values for enough unknowns to leave as many variables as
 there are equations, which in most cases means the system is properly
 defined and a unique solution exists. The function, the fixed values
 and initial values for the remaining unknowns are fed to a nonlinear backsolver.  
 The original version of "TK!Solver" , now a product of Universal Technical Systems (<https://www.uts.com>) was the inspiration for this function.
	"""
	
	cran = "ktsolve" 

	version("1.3.1", md5="c3a47ea112bf4c8479176205f05834ba")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
