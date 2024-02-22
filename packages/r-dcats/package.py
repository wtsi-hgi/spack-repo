# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcats(RPackage):
	"""Differential Composition Analysis Transformed by a Similarity matrix

	Methods to detect the differential composition abundances between conditions in singel-cell RNA-seq experiments, with or without replicates. It aims to correct bias introduced by missclaisification and enable controlling of confounding covariates. To avoid the influence of proportion change from big cell types, DCATS can use either total cell number or specific reference group as normalization term.
	"""
	
	bioc = "DCATS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DCATS_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DCATS/DCATS_1.0.0.tar.gz"]

	version("1.0.0", md5="8a6002426027bd88d05a2b8759d5a12e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
