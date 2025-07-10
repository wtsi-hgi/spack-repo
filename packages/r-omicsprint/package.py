# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicsprint(RPackage):
	"""Cross omic genetic fingerprinting

	omicsPrint provides functionality for cross omic genetic fingerprinting, for example, to verify sample relationships between multiple omics data types, i.e. genomic, transcriptomic and epigenetic (DNA methylation).
	"""
	
	bioc = "omicsPrint" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/omicsPrint_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/omicsPrint/omicsPrint_1.22.0.tar.gz"]

	version("1.22.0", sha256="1672bd2ec21f524cbbf66cccea505d677db036fec53ba0e221a7c57224395d6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
