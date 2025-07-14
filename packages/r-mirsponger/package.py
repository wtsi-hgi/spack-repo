# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirsponger(RPackage):
	"""Identification and analysis of miRNA sponge regulation

	This package provides several functions to explore miRNA sponge (also called ceRNA or miRNA decoy) regulation from putative miRNA-target interactions or/and transcriptomics data (including bulk, single-cell and spatial gene expression data). It provides eight popular methods for identifying miRNA sponge interactions, and an integrative method to integrate miRNA sponge interactions from different methods, as well as the functions to validate miRNA sponge interactions, and infer miRNA sponge modules, conduct enrichment analysis of miRNA sponge modules, and conduct survival analysis of miRNA sponge modules. By using a sample control variable strategy, it provides a function to infer sample-specific miRNA sponge interactions. In terms of sample-specific miRNA sponge interactions, it implements three similarity methods to construct sample-sample correlation network.
	"""
	
	homepage = "<https://github.com/zhangjunpeng411/miRspongeR>"
	bioc = "miRspongeR" 

	version("2.12.0", tag="RELEASE_3_21")
	version("2.6.0", commit="3a9398baefed6c5745b8338df2d91b6f213e4d2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-sponge", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mcl", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-reactomepa", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-linkcomm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
