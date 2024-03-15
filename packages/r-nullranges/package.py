# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNullranges(RPackage):
	"""Generation of null ranges via bootstrapping or covariate matching

	Modular package for generation of sets of ranges representing the null hypothesis. These can take the form of bootstrap samples of ranges (using the block bootstrap framework of Bickel et al 2010), or sets of control ranges that are matched across one or more covariates. nullranges is designed to be inter-operable with other packages for analysis of genomic overlap enrichment, including the plyranges Bioconductor package.
	"""
	
	homepage = "https://nullranges.github.io/nullranges"
	bioc = "nullranges" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nullranges_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nullranges/nullranges_1.8.0.tar.gz"]

	version("1.8.0", md5="6ee32a46c332cfeefa89ebc2b32608bf")

	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
