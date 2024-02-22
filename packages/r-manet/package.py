# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManet(RPackage):
	"""Multiple Allocation Model for Actor-Event Networks

	Mixture model with overlapping clusters for binary actor-event data. Parameters are estimated in a Bayesian framework. Model and inference are described in Ranciati, Vinciotti, Wit (2017) Modelling actor-event network data via a mixture model under overlapping clusters. Submitted.
	"""
	
	cran = "manet" 

	version("2.0", md5="1ff1c323e28e2c91337f3a48e6856a02")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
