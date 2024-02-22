# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBackshift(RPackage):
	"""Learning Causal Cyclic Graphs from Unknown Shift Interventions

	Code for 'backShift', an algorithm to estimate the connectivity
    matrix of a directed (possibly cyclic) graph with hidden variables. The
    underlying system is required to be linear and we assume that observations
    under different shift interventions are available. For more details,
    see <arXiv:1506.02494>.
	"""
	
	homepage = "https://github.com/christinaheinze/backShift"
	cran = "backShift" 

	version("0.1.4.3", md5="b1111ed24a61c786c5d02ea104c23089")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
