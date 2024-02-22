# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBestie(RPackage):
	"""Bayesian Estimation of Intervention Effects

	An implementation of intervention effect estimation for DAGs (directed acyclic graphs) learned from binary or continuous data. First, parameters are estimated or sampled for the DAG and then interventions on each node (variable) are propagated through the network (do-calculus). Both exact computation (for continuous data or for binary data up to around 20 variables) and Monte Carlo schemes (for larger binary networks) are implemented.
	"""
	
	cran = "Bestie" 

	version("0.1.5", md5="2d1935b0edbb71fc1afb0f84d87bd6db")

	depends_on("r-bidag@2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm@1.1:", type=("build", "run"))
