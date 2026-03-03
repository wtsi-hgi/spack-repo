# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicdcplus(RPackage):
	"""Hi-C Direct Caller Plus

	Systematic 3D interaction calls and differential analysis for Hi-C and HiChIP. The HiC-DC+ (Hi-C/HiChIP direct caller plus) package enables principled statistical analysis of Hi-C and HiChIP data sets – including calling significant interactions within a single experiment and performing differential analysis between conditions given replicate experiments – to facilitate global integrative studies. HiC-DC+ estimates significant interactions in a Hi-C or HiChIP experiment directly from the raw contact matrix for each chromosome up to a specified genomic distance, binned by uniform genomic intervals or restriction enzyme fragments, by training a background model to account for random polymer ligation and systematic sources of read count variation.
	"""
	
	bioc = "HiCDCPlus" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HiCDCPlus_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HiCDCPlus/HiCDCPlus_1.10.0.tar.gz"]

	version("1.10.0", md5="d129ae6d6c11f6f92e52399c46754b1f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-genomicinteractions", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
