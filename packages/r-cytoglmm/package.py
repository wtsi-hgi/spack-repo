# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytoglmm(RPackage):
	"""Conditional Differential Analysis for Flow and Mass Cytometry Experiments

	The CytoGLMM R package implements two multiple regression strategies: A bootstrapped generalized linear model (GLM) and a generalized linear mixed model (GLMM). Most current data analysis tools compare expressions across many computationally discovered cell types. CytoGLMM focuses on just one cell type. Our narrower field of application allows us to define a more specific statistical model with easier to control statistical guarantees. As a result, CytoGLMM finds differential proteins in flow and mass cytometry data while reducing biases arising from marker correlations and safeguarding against false discoveries induced by patient heterogeneity.
	"""
	
	homepage = "https://christofseiler.github.io/CytoGLMM"
	bioc = "CytoGLMM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CytoGLMM_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CytoGLMM/CytoGLMM_1.10.0.tar.gz"]

	version("1.10.0", md5="3a4b95062a82da6afe217f20ef905460")

	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mbest", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
