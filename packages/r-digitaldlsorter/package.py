# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigitaldlsorter(RPackage):
	"""Deconvolution of Bulk RNA-Seq Data Based on Deep Learning

	Deconvolution of bulk RNA-Seq data using context-specific deconvolution models based on Deep Neural Networks using scRNA-Seq data as input. These models are able to make accurate estimates of the cell composition of bulk RNA-Seq samples from the same context using the advances provided by Deep Learning and the meaningful information provided by scRNA-Seq data. See Torroja and Sanchez-Cabo (2019) <doi:10.3389/fgene.2019.00978> for more details.
	"""
	
	homepage = "https://diegommcc.github.io/digitalDLSorteR/"
	cran = "digitalDLSorteR" 

	version("1.0.1", md5="814b655f6e9a37e9dffa9e35618f89a5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-grr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-zinbwave", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("python@2.7.0:", type=("build", "link", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
