# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCladorcpp(RPackage):
	"""C++ Implementations of Phylogenetic Cladogenesis Calculations

	Various cladogenesis-related calculations that are slow in pure R are implemented in C++ with Rcpp. These include the calculation of the probability of various scenarios for the inheritance of geographic range at the divergence events on a phylogenetic tree, and other calculations necessary for models which are not continuous-time markov chains (CTMC), but where change instead occurs instantaneously at speciation events.  Typically these models must assess the probability of every possible combination of (ancestor state, left descendent state, right descendent state).  This means that there are up to (# of states)^3 combinations to investigate, and in biogeographical models, there can easily be hundreds of states, so calculation time becomes an issue.  C++ implementation plus clever tricks (many combinations can be eliminated a priori) can greatly speed the computation time over naive R implementations.  CITATION INFO: This package is the result of my Ph.D. research, please cite the package if you use it!  Type: citation(package="cladoRcpp") to get the citation information.
	"""
	
	homepage = "http://phylo.wikidot.com/biogeobears"
	cran = "cladoRcpp" 

	version("0.15.1", md5="11f2d2622212b61f36d3e7ed406a957d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
