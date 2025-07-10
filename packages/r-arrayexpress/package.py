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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ArrayExpress_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ArrayExpress/ArrayExpress_1.62.0.tar.gz"]

	version("1.62.0", sha256="5992297a2d64cfc580a42b7afb0d85597090e1ab412931e0c5e52f9c4d36cb32")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-biobase@2.4:", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
