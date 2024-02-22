# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdephylo(RPackage):
	"""Exploratory Analyses for the Phylogenetic Comparative Method.

	Multivariate tools to analyze comparative data, i.e. a phylogeny and some
	traits measured for each taxa."""

	cran = "adephylo"

	version("1.1-16", md5="bd228e0553cd3d037bdca3fe7bff4bc3")

	depends_on("r-ade4@1.7.10:", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
