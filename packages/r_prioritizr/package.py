# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrioritizr(RPackage):
	"""Systematic Conservation Prioritization in R

	
    Systematic conservation prioritization using mixed integer linear
    programming (MILP). It provides a flexible interface for building and
    solving conservation planning problems. Once built, conservation planning
    problems can be solved using a variety of commercial and open-source exact
    algorithm solvers. By using exact algorithm solvers, solutions can be
    generated that are guaranteed to be optimal (or within a pre-specified
    optimality gap). Furthermore, conservation problems can be constructed to
    optimize the spatial allocation of different management actions or zones,
    meaning that conservation practitioners can identify solutions that benefit
    multiple stakeholders. To solve large-scale or complex conservation
    planning problems, users should install the Gurobi optimization software
    (available from <https://www.gurobi.com/>) and the 'gurobi' R package (see
    Gurobi Installation Guide vignette for details). Users can also install the
    IBM CPLEX software (<https://www.ibm.com/products/ilog-cplex-optimization-studio/cplex-optimizer>) and
    the 'cplexAPI' R package (available at <https://github.com/cran/cplexAPI>).
    Additionally, the 'rcbc' R package (available at
    <https://github.com/dirkschumacher/rcbc>) can be used to generate solutions
    using the CBC optimization software (<https://github.com/coin-or/Cbc>).
	"""
	
	homepage = "https://prioritizr.net"
	cran = "prioritizr" 

	version("8.0.3", md5="66901e7bd97e773d2ec7a86567b056de")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-terra@1.6.53:", type=("build", "run"))
	depends_on("r-raster@3.6.11:", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-slam@0.1.48:", type=("build", "run"))
	depends_on("r-igraph@1.2.9:", type=("build", "run"))
	depends_on("r-ape@5.6.1:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-exactextractr@0.8.1:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-withr@2.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.7.3:", type=("build", "run"))
	depends_on("r-bh@1.75.0.0:", type=("build", "run"))
