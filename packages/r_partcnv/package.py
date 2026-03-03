# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartcnv(RPackage):
	"""Infer locally aneuploid cells using single cell RNA-seq data

	This package uses a statistical framework for rapid and accurate detection of aneuploid cells with local copy number deletion or amplification. Our method uses an EM algorithm with mixtures of Poisson distributions while incorporating cytogenetics information (e.g., regional deletion or amplification) to guide the classification (partCNV). When applicable, we further improve the accuracy by integrating a Hidden Markov Model for feature selection (partCNVH).
	"""
	
	bioc = "partCNV" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/partCNV_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/partCNV/partCNV_1.0.0.tar.gz"]

	version("1.0.0", md5="e004f2129cbb1fe1e84e33cf223c06f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-depmixs4", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
