# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuvcorr(RPackage):
	"""Removal of unwanted variation for gene-gene correlations and related analysis

	RUVcorr allows to apply global removal of unwanted variation (ridged version of RUV) to real and simulated gene expression data.
	"""
	
	bioc = "RUVcorr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RUVcorr_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RUVcorr/RUVcorr_1.34.0.tar.gz"]

	version("1.34.0", md5="cfc2e185bc7d37f264843a6fa5ed7c6d")

	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bladderbatch", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
