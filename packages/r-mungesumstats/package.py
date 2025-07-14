# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMungesumstats(RPackage):
	"""Standardise summary statistics from GWAS

	The *MungeSumstats* package is designed to facilitate the standardisation of GWAS summary statistics. It reformats inputted summary statisitics to include SNP, CHR, BP and can look up these values if any are missing. It also pefrorms dozens of QC and filtering steps to ensure high data quality and minimise inter-study differences.
	"""
	
	homepage = "https://github.com/neurogenomics/MungeSumstats"
	bioc = "MungeSumstats" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MungeSumstats_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MungeSumstats/MungeSumstats_1.10.1.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.1", sha256="d3b1a86d512a0ec9e946444b2515250c11957937ca362268d0f1ad107b77f160")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-googleauthr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rtracklayer@1.59.1:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
