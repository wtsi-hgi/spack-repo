# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdpt3r(RPackage):
	"""Semi-Definite Quadratic Linear Programming Solver

	Solves the general Semi-Definite Linear Programming formulation using an R implementation of SDPT3 (K.C. Toh, M.J. Todd, and R.H. Tutuncu (1999) <doi:10.1080/10556789908805762>). This includes problems such as the nearest correlation matrix problem (Higham (2002) <doi:10.1093/imanum/22.3.329>), D-optimal experimental design (Smith (1918) <doi:10.2307/2331929>), Distance Weighted Discrimination (Marron and Todd (2012) <doi:10.1198/016214507000001120>), as well as graph theory problems including the maximum cut problem. Technical details surrounding SDPT3 can be found in R.H Tutuncu, K.C. Toh, and M.J. Todd (2003) <doi:10.1007/s10107-002-0347-5>. 
	"""
	
	cran = "sdpt3r" 

	version("0.3", md5="5ef447296df9a0e490a369a80eb5ba14")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
