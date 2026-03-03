# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSidier(RPackage):
	"""Substitution and Indel Distances to Infer Evolutionary
Relationships

	Evolutionary reconstruction based on substitutions and insertion-deletion (indels) analyses in a distance-based framework.
	"""
	
	cran = "sidier" 

	version("4.1.0", md5="7d917fa3ea764835283862fb92ab6428")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
