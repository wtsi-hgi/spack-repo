# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDexma(RPackage):
	"""Differential Expression Meta-Analysis

	performing all the steps of gene expression meta-analysis considering the possible existence of missing genes. It provides the necessary functions to be able to perform the different methods of gene expression meta-analysis. In addition, it contains functions to apply quality controls, download GEO datasets and show graphical representations of the results.
	"""
	
	bioc = "DExMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DExMA_1.10.7.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DExMA/DExMA_1.10.7.tar.gz"]

    version("1.16.0", tag="RELEASE_3_21")
	version("1.10.7", sha256="dc1fd3934aa9681ceda6a0676b0c3c7d241249f3cdfaeb93aa1376edd898db8a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dexmadata", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-swamp", type=("build", "run"))
	depends_on("r-bnstruct", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
