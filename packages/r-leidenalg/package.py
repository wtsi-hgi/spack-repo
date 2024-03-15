# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeidenalg(RPackage):
	"""Implements the Leiden Algorithm via an R Interface

	An R interface to the Leiden algorithm, an iterative community detection algorithm on networks. The algorithm is designed to converge to a partition in which all subsets of all communities are locally optimally assigned, yielding communities guaranteed to be connected. The implementation proves to be fast, scales well, and can be run on graphs of millions of nodes (as long as they can fit in memory). The original implementation was constructed as a python interface "leidenalg" found here: <https://github.com/vtraag/leidenalg>. The algorithm was originally described in Traag, V.A., Waltman, L. & van Eck, N.J. "From Louvain to Leiden: guaranteeing well-connected communities". Sci Rep 9, 5233 (2019) <doi:10.1038/s41598-019-41695-z>.
	"""
	
	homepage = "https://github.com/kharchenkolab/leidenAlg"
	cran = "leidenAlg" 

	version("1.1.3", md5="1cfeda2c0df7668f18500ae594019a08")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sccore", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("libxml2", type=("build", "link", "run"))
	depends_on("glpk@4.57:", type=("build", "link", "run"))
