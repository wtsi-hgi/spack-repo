# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignnet(RPackage):
	"""Methods to Analyse Signed Networks

	Methods for the analysis of signed networks. This includes
    several measures for structural balance as introduced by Cartwright
    and Harary (1956) <doi:10.1037/h0046049>, blockmodeling algorithms
    from Doreian (2008) <doi:10.1016/j.socnet.2008.03.005>, various
    centrality indices, and projections of signed two-mode networks
    introduced by Schoch (2020) <doi:10.1080/0022250X.2019.1711376>.
	"""
	
	homepage = "https://github.com/schochastics/signnet"
	cran = "signnet" 

	version("1.0.4", md5="d7d96591cf7c59f11f14e8ef23d5ee6c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
