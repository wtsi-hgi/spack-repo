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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/LRcellTypeMarkers_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/LRcellTypeMarkers/LRcellTypeMarkers_1.10.0.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="4c20c86955b7a8b2ca6fb3a9bcc0ccb4811a26585a474221a237b977193a4df1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

