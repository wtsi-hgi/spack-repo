# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrcelltypemarkers(RPackage):
	"""Marker gene information for LRcell R Bioconductor package

	This is an external ExperimentData package for LRcell. This data package contains the gene enrichment scores calculated from scRNA-seq dataset which indicates the gene enrichment of each cell type in certain brain region. LRcell package is used to identify specific sub-cell types that drives the changes observed in a bulk RNA-seq differential gene expression experiment. For more details, please visit: https://github.com/marvinquiet/LRcell.
	"""
	
	bioc = "LRcellTypeMarkers"

	version("1.16.0", commit="e72248999b7d29cd382fc2e8304a12a1b5636583")
	version("1.10.0", commit="cede01cf22393aa3416be74c82bad4950004637d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

