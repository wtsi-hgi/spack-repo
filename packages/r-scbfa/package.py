# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbfa(RPackage):
	"""A dimensionality reduction tool using gene detection pattern to mitigate noisy expression profile of scRNA-seq

	This package is designed to model gene detection pattern of scRNA-seq through a binary factor analysis model. This model allows user to pass into a cell level covariate matrix X and gene level covariate matrix Q to account for nuisance variance(e.g batch effect), and it will output a low dimensional embedding matrix for downstream analysis.
	"""
	
	homepage = "https://github.com/ucdavis/quon-titative-biology/BFA"
	bioc = "scBFA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scBFA_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scBFA/scBFA_1.16.0.tar.gz"]

	version("1.16.0", sha256="a3c5c70ce0740f931db630a73ac86bf78b9fb31788a15e7be188f814d8dc6481")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-zinbwave", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
