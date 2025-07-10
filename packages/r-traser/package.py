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

	version("1.32.0", sha256="38a4fa6f092e86671a646dcdc9c46cd077fafab3a9f37c86856aa3ff5800b117")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
