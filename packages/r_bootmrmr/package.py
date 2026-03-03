# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootmrmr(RPackage):
	"""Bootstrap-MRMR Technique for Informative Gene Selection

	Selection of informative features like genes, transcripts, RNA seq, etc. using Bootstrap Maximum Relevance and Minimum Redundancy technique from a given high dimensional genomic dataset. Informative gene selection involves identification of relevant genes and removal of redundant genes as much as possible from a large gene space. Main applications in high-dimensional expression data analysis (e.g. microarray data, NGS expression data and other genomics and proteomics applications).
	"""
	
	cran = "BootMRMR" 

	version("0.1", md5="1a441eb0bc3e351152e68fc00aa1b0c7")

	depends_on("r@3.3.1:", type=("build", "run"))
