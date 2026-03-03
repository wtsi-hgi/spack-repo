# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygenomics(RPackage):
	"""Tidy Verbs for Dealing with Genomic Data Frames

	Handle genomic data within data frames just as you would with 'GRanges'.
    This packages provides method to deal with genomic intervals the "tidy-way" which makes
    it simpler to integrate in the the general data munging process. The API is inspired by the
    popular 'bedtools' and the genome_join() method from the 'fuzzyjoin' package.
	"""
	
	homepage = "https://github.com/const-ae/tidygenomics"
	cran = "tidygenomics" 

	version("0.1.2", md5="fa1b7224b21714f33531a777cf9a6dcb")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fuzzyjoin@0.1.3:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
