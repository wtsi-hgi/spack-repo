# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAeenrich(RPackage):
	"""Adverse Event Enrichment Tests

	We extend existing gene enrichment tests to perform adverse
    event enrichment analysis. Unlike the continuous gene expression data,
    adverse event data are counts. Therefore, adverse event data has many zeros
    and ties. We propose two enrichment tests. One is a modified Fisher's exact
    test based on pre-selected significant adverse events, while the other is
    based on a modified Kolmogorov-Smirnov statistic. We add Covariate
    adjustment to improve the analysis."Adverse event enrichment tests using
    VAERS" Shuoran Li, Lili Zhao (2020) <arXiv:2007.02266>.
	"""
	
	homepage = "https://github.com/umich-biostatistics/AEenrich"
	cran = "AEenrich" 

	version("1.1.0", md5="d5ee54ce59c04c2820a58aceb79883ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
