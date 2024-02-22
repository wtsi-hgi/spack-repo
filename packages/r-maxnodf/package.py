# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxnodf(RPackage):
	"""Approximate Maximisation of Nestedness in Bipartite Graphs

	Functions to generate graphs that maximise the NODF (nestedness metric based
    on overlap and decreasing fill) metric for a given number of rows, columns
    and links. NODF was originally defined by Almeida-Neto et al. (2008)
    <doi:10.1111/j.0030-1299.2008.16644.x>. As nestedness in ecological networks
    depends on the size of the networks we require normalisation to make them
    comparable. We offer three highly optimised algorithms to find the
    optimising graphs so that users can choose an appropriate trade off between
    computation time and NODF value for the task at hand.
	"""
	
	cran = "maxnodf" 

	version("1.0.0", md5="4c6933157a9f5ad7b074399468d6b9b1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
