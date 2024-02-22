# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcorr(RPackage):
	"""CONCOR and Supplemental Functions

	Contains the CONCOR (CONvergence of iterated CORrelations) 
    algorithm and a series of supplemental functions for easy running, 
    plotting, and blockmodeling. The CONCOR algorithm is used on social network
    data to identify network positions based off a definition of structural 
    equivalence; see Breiger, Boorman, and Arabie (1975) 
    <doi:10.1016/0022-2496(75)90028-0> and Wasserman and Faust's book Social 
    Network Analysis: Methods and Applications (1994). This version allows 
    multiple relationships for the same set of nodes and uses both incoming and
    outgoing ties to find positions.
	"""
	
	homepage = "https://github.com/ATraxLab/concorR"
	cran = "concorR" 

	version("0.2.1", md5="f40fb7dffdaaeb23e4ce859669c1d895")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
