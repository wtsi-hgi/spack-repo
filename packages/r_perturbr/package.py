# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerturbr(RPackage):
	"""Random Perturbation of Count Matrices

	The perturbR() function incrementally perturbs network edges (using the   rewireR function)and compares the resulting community detection solutions 
    from the rewired networks with the solution found for the original network. 
    These comparisons aid in understanding the stability of the 
    original solution. The package requires symmetric, weighted (specifically, count) matrices/networks.
	"""
	
	cran = "perturbR" 

	version("0.1.3", md5="81dc16129fc435d0b2e1a264581a9e6f")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
