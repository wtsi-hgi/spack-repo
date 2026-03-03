# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBidag(RPackage):
	"""Bayesian Inference for Directed Acyclic Graphs

	Implementation of a collection of MCMC methods for Bayesian structure learning
    of directed acyclic graphs (DAGs), both from continuous and discrete data. For efficient
    inference on larger DAGs, the space of DAGs is pruned according to the data. To filter
    the search space, the algorithm employs a hybrid approach, combining constraint-based 
    learning with search and score. A reduced search space is initially defined on the basis
    of a skeleton obtained by means of the PC-algorithm, and then iteratively improved with
    search and score. Search and score is then performed following two approaches:
    Order MCMC, or Partition MCMC.
    The BGe score is implemented for continuous data and the BDe score is implemented
    for binary data or categorical data. The algorithms may provide the maximum a posteriori 
    (MAP) graph or a sample (a collection of DAGs) from the posterior distribution given the data.
    All algorithms are also applicable for structure learning and sampling for dynamic Bayesian networks.
    References:
    J. Kuipers, P. Suter, G. Moffa (2022) <doi:10.1080/10618600.2021.2020127>,
    N. Friedman and D. Koller (2003) <doi:10.1023/A:1020249912095>, 
    J. Kuipers and G. Moffa (2017) <doi:10.1080/01621459.2015.1133426>, 
    M. Kalisch et al. (2012) <doi:10.18637/jss.v047.i11>,
    D. Geiger and D. Heckerman (2002) <doi:10.1214/aos/1035844981>, 
    P. Suter, J. Kuipers, G. Moffa, N.Beerenwinkel (2023) <doi:10.18637/jss.v105.i09>.
	"""
	
	cran = "BiDAG" 

	version("2.1.4", md5="e6ad7201bb712454b0dbd9bc377539d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
