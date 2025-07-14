# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelocal(RPackage):
	"""Identifies differentially expressed genes with respect to other local genes

	The goal of DELocal is to identify DE genes compared to their neighboring genes from the same chromosomal location. It has been shown that genes of related functions are generally very far from each other in the chromosome. DELocal utilzes this information to identify DE genes comparing with their neighbouring genes.
	"""
	
	homepage = "https://github.com/dasroy/DELocal"
	bioc = "DELocal"

	version("1.8.0", commit="960dacb70da81d0bfa4ee4cd08f5debc9987c8f7")
	version("1.2.1", commit="063d5230468f9337e3ab737d817ec5e6a07ab0b6")
	version("1.2.0", md5="40f2eac89260ff4692fb02047990d048")

	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
