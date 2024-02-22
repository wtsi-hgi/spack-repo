# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDodgr(RPackage):
	"""Distances on Directed Graphs

	Distances on dual-weighted directed graphs using
    priority-queue shortest paths (Padgham (2019) <doi:10.32866/6945>).
    Weighted directed graphs have weights from A to B which may differ
    from those from B to A.  Dual-weighted directed graphs have two sets
    of such weights. A canonical example is a street network to be used
    for routing in which routes are calculated by weighting distances
    according to the type of way and mode of transport, yet lengths of
    routes must be calculated from direct distances.
	"""
	
	homepage = "https://github.com/ATFutures/dodgr"
	cran = "dodgr" 

	version("0.2.21", md5="2d43e2c7ad5cb8ac82462aad1085bdfb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-osmdata", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
