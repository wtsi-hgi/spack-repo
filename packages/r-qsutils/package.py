# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsutils(RPackage):
	"""Quasispecies Diversity

	Set of utility functions for viral quasispecies analysis with NGS data. Most functions are equally useful for metagenomic studies. There are three main types: (1) data manipulation and exploration—functions useful for converting reads to haplotypes and frequencies, repairing reads, intersecting strand haplotypes, and visualizing haplotype alignments. (2) diversity indices—functions to compute diversity and entropy, in which incidence, abundance, and functional indices are considered. (3) data simulation—functions useful for generating random viral quasispecies data.
	"""
	
	bioc = "QSutils" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/QSutils_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/QSutils/QSutils_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="d964b12cf00cdf9ca665bddc2e56083b3a5e6a2751e5605790c7ce7894ac238c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
