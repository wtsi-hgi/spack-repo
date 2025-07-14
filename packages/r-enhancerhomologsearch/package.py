# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnhancerhomologsearch(RPackage):
	"""Identification of putative mammalian orthologs to given enhancer

	Get ENCODE data of enhancer region via H3K4me1 peaks and search homolog regions for given sequences. The candidates of enhancer homolog regions can be filtered by distance to target TSS. The top candidates from human and mouse will be aligned to each other and then exported as multiple alignments with given enhancer.
	"""
	
	homepage = "https://jianhong.github.io/enhancerHomologSearch"
	bioc = "enhancerHomologSearch" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/enhancerHomologSearch_1.8.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/enhancerHomologSearch/enhancerHomologSearch_1.8.3.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.3", sha256="827c545a6bb9a0102b2e23332ead594af7aad6edb34251b7daaaed0c10c588d3")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
