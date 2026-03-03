# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicroseq(RPackage):
	"""Basic Biological Sequence Handling

	Basic functions for microbial sequence data analysis. The idea is to use generic R data structures as much as possible, making R data wrangling possible also for sequence data.
	"""
	
	cran = "microseq" 

	version("2.1.6", md5="14d090ce4d386d2480b9be55622ac46b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
