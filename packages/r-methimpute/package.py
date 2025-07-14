# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethimpute(RPackage):
	"""Imputation-guided re-construction of complete methylomes from WGBS data

	This package implements functions for calling methylation for all cytosines in the genome.
	"""
	
	bioc = "methimpute" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/methimpute_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/methimpute/methimpute_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="16efff43478e8d2a09d80c4e6475eeb654f4936eb06fa28578face1de7eabb69")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
