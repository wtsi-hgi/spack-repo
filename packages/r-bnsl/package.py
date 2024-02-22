# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnsl(RPackage):
	"""Bayesian Network Structure Learning

	From a given data frame, this package learns its Bayesian network structure based on a selected score.
	"""
	
	cran = "BNSL" 

	version("0.1.4", md5="8a3232b1bf90767bee5127c9c9311551")

	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
