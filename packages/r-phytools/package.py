# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhytools(RPackage):
	"""Phylogenetic Tools for Comparative Biology (and Other Things).

	A wide range of functions for phylogenetic analysis. Functionality is
	concentrated in phylogenetic comparative biology, but also includes
	numerous methods for visualizing, manipulating, reading or writing, and
	even inferring phylogenetic trees and data. Included among the functions in
	phylogenetic comparative biology are various for ancestral state
	reconstruction, model-fitting, simulation of phylogenies and data, and
	multivariate analysis. There are a broad range of plotting methods for
	phylogenies and comparative data which include, but are not restricted to,
	methods for mapping trait evolution on trees, for projecting trees into
	phenotypic space or a geographic map, and for visualizing correlated
	speciation between trees. Finally, there are a number of functions for
	reading, writing, analyzing, inferring, simulating, and manipulating
	phylogenetic trees and comparative data not covered by other packages. For
	instance, there are functions for randomly or non-randomly attaching
	species or clades to a phylogeny, for estimating supertrees or consensus
	phylogenies from a set, for simulating trees and phylogenetic data under a
	range of models, and for a wide variety of other manipulations and analyses
	that phylogenetic biologists might find useful in their research."""

	cran = "phytools"

	version("2.1-1", md5="b03442df6f468772b8da8784eef396e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@5.7:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
	depends_on("r-phangorn@2.3.1:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
