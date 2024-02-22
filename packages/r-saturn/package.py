# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaturn(RPackage):
	"""Scalable Analysis of Differential Transcript Usage for Bulk and Single-Cell RNA-sequencing Applications

	satuRn provides a higly performant and scalable framework for performing differential transcript usage analyses. The package consists of three main functions. The first function, fitDTU, fits quasi-binomial generalized linear models that model transcript usage in different groups of interest. The second function, testDTU, tests for differential usage of transcripts between groups of interest. Finally, plotDTU visualizes the usage profiles of transcripts in groups of interest.
	"""
	
	homepage = "https://github.com/statOmics/satuRn"
	bioc = "satuRn" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/satuRn_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/satuRn/satuRn_1.10.0.tar.gz"]

	version("1.10.0", md5="a0826944ab0aee6ff42127fa7eebf43c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
