# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrnastat(RPackage):
	"""A Pipeline to Process Single Cell RNAseq Data

	A pipeline that can process single or multiple Single Cell RNAseq 
    samples primarily specializes in Clustering and Dimensionality Reduction. 
    Meanwhile we use common cell type marker genes for T cells, B cells, Myeloid cells, 
    Epithelial cells, and stromal cells (Fiboblast, Endothelial cells, Pericyte,
    Smooth muscle cells) to visualize the Seurat clusters, to facilitate labeling 
    them by biological names. Once users named each cluster, they can evaluate the 
    quality of them again and find the de novo marker genes also.
	"""
	
	cran = "scRNAstat" 

	version("0.1.1", md5="241e085957b2b467c492274b14373730")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-clustree", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
