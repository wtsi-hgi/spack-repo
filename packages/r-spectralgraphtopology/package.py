# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectralgraphtopology(RPackage):
	"""Learning Graphs from Data via Spectral Constraints

	In the era of big data and hyperconnectivity, learning
    high-dimensional structures such as graphs from data has become a prominent
    task in machine learning and has found applications in many fields such as
    finance, health care, and networks. 'spectralGraphTopology' is an open source,
    documented, and well-tested R package for learning graphs from data. It
    provides implementations of state of the art algorithms such as Combinatorial
    Graph Laplacian Learning (CGL), Spectral Graph Learning (SGL), Graph Estimation
    based on Majorization-Minimization (GLE-MM), and Graph Estimation based on
    Alternating Direction Method of Multipliers (GLE-ADMM). In addition, graph
    learning has been widely employed for clustering, where specific algorithms
    are available in the literature. To this end, we provide an implementation of
    the Constrained Laplacian Rank (CLR) algorithm.
	"""
	
	homepage = "https://github.com/dppalomar/spectralGraphTopology"
	cran = "spectralGraphTopology" 

	version("0.2.3", md5="d4fd864614d7c2613b3a4d4743cd271f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
