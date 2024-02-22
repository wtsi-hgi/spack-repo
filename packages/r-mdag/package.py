# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdag(RPackage):
	"""Inferring Causal Network from Mixed Observational Data Using a
Directed Acyclic Graph

	Learning a mixed directed acyclic graph based on both continuous and categorical data.
	"""
	
	cran = "mDAG" 

	version("1.2.2", md5="eebeb524c7e9be908ffebc757235cc7b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-mgm", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
