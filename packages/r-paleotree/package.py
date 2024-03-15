# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RPaleotree(RPackage):
	"""Paleontological and Phylogenetic Analyses of Evolution.

	Provides tools for transforming, a posteriori time-scaling, and modifying
	phylogenies containing extinct (i.e. fossil) lineages"""

	cran = "paleotree"

	license("CC0-1.0")

	version("3.4.5", md5="ebd2771e32927e4a9f21d06b805d59df")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ape@4.1:", type=("build", "run"))
	depends_on("r-phangorn@2.6.3:", type=("build", "run"))
	depends_on("r-phytools@0.6.00:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
