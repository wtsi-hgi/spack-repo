# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidecoder(RPackage):
	"""epidecodeR: a functional exploration tool for epigenetic and epitranscriptomic regulation

	epidecodeR is a package capable of analysing impact of degree of DNA/RNA epigenetic chemical modifications on dysregulation of genes or proteins. This package integrates chemical modification data generated from a host of epigenomic or epitranscriptomic techniques such as ChIP-seq, ATAC-seq, m6A-seq, etc. and dysregulated gene lists in the form of differential gene expression, ribosome occupancy or differential protein translation and identify impact of dysregulation of genes caused due to varying degrees of chemical modifications associated with the genes. epidecodeR generates cumulative distribution function (CDF) plots showing shifts in trend of overall log2FC between genes divided into groups based on the degree of modification associated with the genes. The tool also tests for significance of difference in log2FC between groups of genes.
	"""
	
	homepage = "https://github.com/kandarpRJ/epidecodeR"
	bioc = "epidecodeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epidecodeR_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epidecodeR/epidecodeR_1.10.0.tar.gz"]

	version("1.10.0", sha256="97e89cec2638a33e7ddec2b30aa56b2b4d0f865c4b27e4669291ba5e0d0a0705")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
