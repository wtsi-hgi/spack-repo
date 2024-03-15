# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqarray(RPackage):
	"""Data Management of Large-Scale Whole-Genome Sequence Variant Calls

	Data management of large-scale whole-genome sequencing variant calls with thousands of individuals: genotypic data (e.g., SNVs, indels and structural variation calls) and annotations in SeqArray GDS files are stored in an array-oriented and compressed manner, with efficient data access using the R programming language.
	"""
	
	homepage = "https://github.com/zhengxwen/SeqArray"
	bioc = "SeqArray" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SeqArray_1.42.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SeqArray/SeqArray_1.42.2.tar.gz"]

	version("1.42.2", md5="bc97547c09a0e4c30a7a2828b2493367")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
