# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScapgnn(RPackage):
	"""Graph Neural Network-Based Framework for Single Cell Active
Pathways and Gene Modules Analysis

	It is a single cell active pathway analysis tool based on the graph neural network (F. Scarselli (2009) <doi:10.1109/TNN.2008.2005605>; Thomas N. Kipf (2017) <arXiv:1609.02907v4>) to construct the gene-cell association network, infer pathway activity scores from different single cell modalities data, integrate multiple modality data on the same cells into one pathway activity score matrix, identify cell phenotype activated gene modules and parse association networks of gene modules under multiple cell phenotype. In addition, abundant visualization programs are provided to display the results.
	"""
	
	cran = "scapGNN" 

	version("0.1.4", md5="28a339845dda406a8fe99033e97b0624")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-activepathways", type=("build", "run"))
	depends_on("r-adaptgauss", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
