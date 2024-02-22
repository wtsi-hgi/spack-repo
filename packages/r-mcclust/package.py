# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcclust(RPackage):
	"""Process an MCMC Sample of Clusterings

	Implements methods for processing a sample of (hard)
        clusterings, e.g. the MCMC output of a Bayesian clustering
        model. Among them are methods that find a single best
        clustering to represent the sample, which are based on the
        posterior similarity matrix or a relabelling algorithm.
	"""
	
	cran = "mcclust" 

	version("1.0.1", md5="481a105f0cff8e8cf47f432b20367761")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
