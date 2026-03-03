# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScannotate(RPackage):
	"""An Automated Cell Type Annotation Tool for Single-Cell
RNA-Sequencing Data

	An entirely data-driven cell type annotation tools, which requires training data to learn the classifier, but not biological knowledge to make subjective decisions. It consists of three steps: preprocessing training and test data, model fitting on training data, and cell classification on test data. See Xiangling Ji,Danielle Tsao, Kailun Bai, Min Tsao, Li Xing, Xuekui Zhang.(2022)<doi:10.1101/2022.02.19.481159> for more details. 
	"""
	
	homepage = "https://doi.org/10.1101/2022.02.19.481159"
	cran = "scAnnotate" 

	version("0.3", md5="be8dbd2f17569971d02871df78acc3ee")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-seurat@5.0.1:", type=("build", "run"))
	depends_on("r-harmony", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
