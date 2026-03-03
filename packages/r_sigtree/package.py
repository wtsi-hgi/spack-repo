# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigtree(RPackage):
	"""Identify and Visualize Significantly Responsive Branches in a
Phylogenetic Tree

	Provides tools to identify and visualize branches in a phylogenetic tree that are significantly responsive to some intervention, taking as primary inputs a phylogenetic tree (of class phylo) and a data frame (or matrix) of corresponding tip (OTU) labels and p-values.
	"""
	
	cran = "SigTree" 

	version("1.10.6", md5="c05f32a646fe76a79d65e8614ecb1495")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-phyext2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
