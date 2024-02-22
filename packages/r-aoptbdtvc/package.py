# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAoptbdtvc(RPackage):
	"""A-Optimal Block Designs for Comparing Test Treatments with
Controls

	A collection of functions to construct A-optimal block designs for comparing test treatments with one or more control(s). Mainly A-optimal balanced treatment incomplete block designs, weighted A-optimal balanced treatment incomplete block designs, A-optimal group divisible treatment designs and A-optimal balanced bipartite block designs can be constructed using the package. The designs are constructed using algorithms based on linear integer programming. To the best of our knowledge, these facilities to construct A-optimal block designs for comparing test treatments with one or more controls are not available in the existing R packages. For more details on designs for tests versus control(s) comparisons, please see Hedayat, A. S. and Majumdar, D. (1984) <doi:10.1080/00401706.1984.10487989> A-Optimal Incomplete Block Designs for Control-Test Treatment Comparisons, Technometrics, 26, 363-370 and Mandal, B. N. , Gupta, V. K., Parsad, Rajender. (2017) <doi:10.1080/03610926.2015.1071394> Balanced treatment incomplete block designs through integer programming. Communications in Statistics - Theory and Methods 46(8), 3728-3737. 
	"""
	
	cran = "Aoptbdtvc" 

	version("0.0.3", md5="3fa0fa9e5714586981706b6943a90b5f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
