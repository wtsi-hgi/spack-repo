# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdnet(RPackage):
	"""Weighted and Directed Networks

	Assortativity coefficients, centrality measures, 
    and clustering coefficients for weighted and directed networks.
    Rewiring unweighted networks with given assortativity coefficients.
    Generating general preferential attachment networks.
	"""
	
	homepage = "https://gitlab.com/wdnetwork/wdnet"
	cran = "wdnet" 

	version("1.2.3", md5="12c97bb9853cfc030071914b85ab49f8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-rcppxptrutils", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
