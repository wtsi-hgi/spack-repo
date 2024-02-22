# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylmix(RPackage):
	"""MethylMix: Identifying methylation driven cancer genes

	MethylMix is an algorithm implemented to identify hyper and hypomethylated genes for a disease. MethylMix is based on a beta mixture model to identify methylation states and compares them with the normal DNA methylation state. MethylMix uses a novel statistic, the Differential Methylation value or DM-value defined as the difference of a methylation state with the normal methylation state. Finally, matched gene expression data is used to identify, besides differential, functional methylation states by focusing on methylation changes that effect gene expression. References: Gevaert 0. MethylMix: an R package for identifying DNA methylation-driven genes. Bioinformatics (Oxford, England). 2015;31(11):1839-41. doi:10.1093/bioinformatics/btv020. Gevaert O, Tibshirani R, Plevritis SK. Pancancer analysis of DNA methylation-driven genes using MethylMix. Genome Biology. 2015;16(1):17. doi:10.1186/s13059-014-0579-8.
	"""
	
	bioc = "MethylMix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MethylMix_2.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MethylMix/MethylMix_2.32.0.tar.gz"]

	version("2.32.0", md5="4a716254f6aff8e65daf63cdcd939704")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rpmm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
