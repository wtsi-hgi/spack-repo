# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsean(RPackage):
	"""Gene Set Enrichment Analysis with Networks

	Biological molecules in a living organism seldom work individually. They usually interact each other in a cooperative way. Biological process is too complicated to understand without considering such interactions. Thus, network-based procedures can be seen as powerful methods for studying complex process. However, many methods are devised for analyzing individual genes. It is said that techniques based on biological networks such as gene co-expression are more precise ways to represent information than those using lists of genes only. This package is aimed to integrate the gene expression and biological network. A biological network is constructed from gene expression data and it is used for Gene Set Enrichment Analysis.
	"""
	
	bioc = "gsean"

	version("1.28.0", commit="32e4cd38dc1e66bde70217ed2741303e02006806")
	version("1.22.0", commit="c195cedb2890aaab5f0b4f951cc964735980ca23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fgsea", type=("build", "run"))
	depends_on("r-ppinfer", type=("build", "run"))
