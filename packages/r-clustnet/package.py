# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustnet(RPackage):
	"""Network-Based Clustering

	Network-based clustering using a Bayesian network mixture model with optional covariate adjustment.
	"""
	
	cran = "clustNet" 

	version("1.2.0", md5="d93f5978d8d45adf13dfcdb8f08bf372")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bidag@2.0.2:", type=("build", "run"))
	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
