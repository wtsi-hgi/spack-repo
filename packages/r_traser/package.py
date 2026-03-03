# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraser(RPackage):
	"""GWAS trait-associated SNP enrichment analyses in genomic intervals

	traseR performs GWAS trait-associated SNP enrichment analyses in genomic intervals using different hypothesis testing approaches, also provides various functionalities to explore and visualize the results.
	"""
	
	bioc = "traseR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/traseR_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/traseR/traseR_1.32.0.tar.gz"]

	version("1.32.0", md5="2af018d9562b672f6701de644617856b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
