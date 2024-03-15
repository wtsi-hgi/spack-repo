# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaexprs(RPackage):
	"""Generating Samples of Gene Expression Data with Variational Autoencoders

	A fundamental problem in biomedical research is the low number of observations, mostly due to a lack of available biosamples, prohibitive costs, or ethical reasons. By augmenting a few real observations with artificially generated samples, their analysis could lead to more robust and higher reproducible. One possible solution to the problem is the use of generative models, which are statistical models of data that attempt to capture the entire probability distribution from the observations. Using the variational autoencoder (VAE), a well-known deep generative model, this package is aimed to generate samples with gene expression data, especially for single-cell RNA-seq data. Furthermore, the VAE can use conditioning to produce specific cell types or subpopulations. The conditional VAE (CVAE) allows us to create targeted samples rather than completely random ones.
	"""
	
	bioc = "VAExprs" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/VAExprs_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/VAExprs/VAExprs_1.8.0.tar.gz"]

	version("1.8.0", md5="6f9ed6eba476abd7908d6849381b545c")

	depends_on("r-keras", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-catencoders", type=("build", "run"))
	depends_on("r-deeppincs", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
