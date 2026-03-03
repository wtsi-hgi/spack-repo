# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpprouting(RPackage):
	"""Algorithms for Routing and Solving the Traffic Assignment
Problem

	Calculation of distances, shortest paths and isochrones on weighted graphs using several variants of Dijkstra algorithm.
    Proposed algorithms are unidirectional Dijkstra (Dijkstra, E. W. (1959) <doi:10.1007/BF01386390>),
    bidirectional Dijkstra (Goldberg, Andrew & Fonseca F. Werneck, Renato (2005) <https://archive.siam.org/meetings/alenex05/papers/03agoldberg.pdf>),
    A* search (P. E. Hart, N. J. Nilsson et B. Raphael (1968) <doi:10.1109/TSSC.1968.300136>),
    new bidirectional A* (Pijls & Post (2009) <https://repub.eur.nl/pub/16100/ei2009-10.pdf>),
    Contraction hierarchies (R. Geisberger, P. Sanders, D. Schultes and D. Delling (2008) <doi:10.1007/978-3-540-68552-4_24>),
    PHAST (D. Delling, A.Goldberg, A. Nowatzyk, R. Werneck (2011) <doi:10.1016/j.jpdc.2012.02.007>).
    Algorithms for solving the traffic assignment problem are All-or-Nothing assignment,
    Method of Successive Averages,
    Frank-Wolfe algorithm (M. Fukushima (1984) <doi:10.1016/0191-2615(84)90029-8>),
    Conjugate and Bi-Conjugate Frank-Wolfe algorithms (M. Mitradjieva, P. O. Lindberg (2012) <doi:10.1287/trsc.1120.0409>),
    Algorithm-B (R. B. Dial (2006) <doi:10.1016/j.trb.2006.02.008>).
	"""
	
	homepage = "https://github.com/vlarmet/cppRouting"
	cran = "cppRouting" 

	version("3.1", md5="f5fce5166576a1fcfe2bf33e3b3cf6a5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
