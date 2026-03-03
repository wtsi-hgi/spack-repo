# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElectionsDtree(RPackage):
	"""Ranked Voting Election Audits with Dirichlet-Trees

	Perform ballot-polling Bayesian audits for ranked voting elections
    using Dirichlet-tree prior distributions. Everest et al. (2022)
    <arXiv:2206.14605>, <arXiv:2209.03881>.
	"""
	
	homepage = "https://fleverest.github.io/elections.dtree/"
	cran = "elections.dtree" 

	version("2.0.0", md5="5158f448b08b483924b49d2b16d494f1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-prefio@0.1.1:", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
