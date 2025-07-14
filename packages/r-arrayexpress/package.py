# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrayexpress(RPackage):
	"""Access the ArrayExpress Collection at EMBL-EBI Biostudies and build Bioconductor data structures: ExpressionSet, AffyBatch, NChannelSet

	Access the ArrayExpress Collection at EMBL-EBI Biostudies and build Bioconductor data structures: ExpressionSet, AffyBatch, NChannelSet.
	"""
	
	bioc = "ArrayExpress"

	version("1.68.0", commit="291c677792b4919752f5855a1a50e3c368106d40")
	version("1.62.0", commit="52f3e7caae1845336819875b1f3214f93ea0f3bf")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-biobase@2.4:", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
