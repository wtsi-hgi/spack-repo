# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdbasedufe(RPackage):
	"""Tensor Decomposition Based Unsupervised Feature Extraction

	This is a comprehensive package to perform Tensor decomposition based unsupervised feature extraction. It can perform unsupervised feature extraction. It uses tensor decomposition. It is applicable to gene expression, DNA methylation, and histone modification etc. It can perform multiomics analysis. It is also potentially applicable to single cell omics data sets.
	"""
	
	homepage = "https://github.com/tagtag/TDbasedUFE"
	bioc = "TDbasedUFE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TDbasedUFE_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TDbasedUFE/TDbasedUFE_1.2.0.tar.gz"]

    version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="66ed99fd2677d840b52079fd72eaaea8c67e0be06a87e8eba26848e6629514d8")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-mofadata", type=("build", "run"))
	depends_on("r-tximport", type=("build", "run"))
	depends_on("r-tximportdata", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
