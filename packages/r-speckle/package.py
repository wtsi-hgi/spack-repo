# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeckle(RPackage):
	"""Statistical methods for analysing single cell RNA-seq data

	The speckle package contains functions for the analysis of single cell RNA-seq data. The speckle package currently contains functions to analyse differences in cell type proportions. There are also functions to estimate the parameters of the Beta distribution based on a given counts matrix, and a function to normalise a counts matrix to the median library size. There are plotting functions to visualise cell type proportions and the mean-variance relationship in cell type proportions and counts. As our research into specialised analyses of single cell data continues we anticipate that the package will be updated with new functions.
	"""
	
	bioc = "speckle" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/speckle_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/speckle/speckle_1.2.0.tar.gz"]

	version("1.2.0", md5="4603cad300c83d6e6374e5989b5fe32a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
