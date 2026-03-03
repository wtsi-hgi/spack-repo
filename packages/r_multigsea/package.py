# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultigsea(RPackage):
	"""Combining GSEA-based pathway enrichment with multi omics data integration

	Extracted features from pathways derived from 8 different databases (KEGG, Reactome, Biocarta, etc.) can be used on transcriptomic, proteomic, and/or metabolomic level to calculate a combined GSEA-based enrichment score.
	"""
	
	homepage = "https://github.com/yigbt/multiGSEA"
	bioc = "multiGSEA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/multiGSEA_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/multiGSEA/multiGSEA_1.12.0.tar.gz"]

	version("1.12.0", md5="4f22605155c363e634e9a2ca6afae5c3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-graphite", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-metaboliteidmapping", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
