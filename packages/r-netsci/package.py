# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetsci(RPackage):
	"""Calculates Basic Network Measures Commonly Used in Network
Medicine

	Calculates network measures such as Largest Connected Component (LCC), Proximity, Separation, Jaccard Index, 
    along with permutation, when needed. 
	"""
	
	cran = "NetSci" 

	version("1.0.0", md5="0dbe2691a0bd5f31a18f8254d4036e58")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-wto", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-binr", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
