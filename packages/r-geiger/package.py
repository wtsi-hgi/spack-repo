# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeiger(RPackage):
	"""Analysis of Evolutionary Diversification.

	Methods for fitting macroevolutionary models to phylogenetic trees  Pennell
	(2014) <doi:10.1093/bioinformatics/btu181>."""

	cran = "geiger"

	version("2.0.11", md5="925b2f26920deb3a65dc6b8e7bc96f52")

	depends_on("r-ape@3.0.6:", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-phytools@1.5.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-desolve@1.7:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ncbit", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
