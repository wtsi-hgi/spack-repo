# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchmarking(RPackage):
	"""Benchmark and Frontier Analysis Using DEA and SFA

	Methods for frontier
    analysis, Data Envelopment Analysis (DEA), under different
    technology assumptions (fdh, vrs, drs, crs, irs, add/frh, and fdh+),
    and using different efficiency measures (input based, output based,
    hyperbolic graph, additive, super, and directional efficiency). Peers
    and slacks are available, partial price information can be included,
    and optimal cost, revenue and profit can be calculated. Evaluation of
    mergers is also supported.  Methods for graphing the technology sets
    are also included. There is also support for comparative methods based
    on Stochastic Frontier Analyses (SFA) and for convex nonparametric 
    least squares of convex functions (STONED). In general, the methods 
    can be used to solve not only standard models, but also many other 
    model variants. It complements the book, Bogetoft and Otto,
    Benchmarking with DEA, SFA, and R, Springer-Verlag, 2011, but can of
    course also be used as a stand-alone package.
	"""
	
	cran = "Benchmarking" 

	version("0.32", md5="1f0744873f6c41d896d3fb0f094be0ca")
	version("0.31", md5="136460e58c711ed9cc1cdbdbde2e5b86")

	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
