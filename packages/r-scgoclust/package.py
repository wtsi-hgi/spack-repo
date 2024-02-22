# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScgoclust(RPackage):
	"""Measuring Cell Type Similarity with Gene Ontology in Single-Cell
RNA-Seq

	Traditional methods for analyzing single cell RNA-seq datasets focus solely on gene expression, but this package introduces a novel approach that goes beyond this limitation. Using Gene Ontology terms as features, the package allows for the functional profile of cell populations, and comparison within and between datasets from the same or different species. Our approach enables the discovery of previously unrecognized functional similarities and differences between cell types and has demonstrated success in identifying cell types' functional correspondence even between evolutionarily distant species.
	"""
	
	homepage = "https://github.com/Papatheodorou-Group/scGOclust"
	cran = "scGOclust" 

	version("0.2.1", md5="41be599d41e6f4321de7990e8b56a82f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-seurat@5:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-slanter", type=("build", "run"))
