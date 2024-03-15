# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenenmf(RPackage):
	"""Non-Negative Matrix Factorization for Single-Cell Omics

	A collection of methods to extract gene programs from single-cell gene expression data using non-negative matrix factorization (NMF). 'GeneNMF' contains functions to directly interact with the 'Seurat' toolkit and derive interpretable gene program signatures.
	"""
	
	homepage = "https://github.com/carmonalab/GeneNMF"
	cran = "GeneNMF" 

	version("0.4.0", md5="5600bad6347549fc2619ff55b8e50538")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcppml", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-seurat@4.3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
