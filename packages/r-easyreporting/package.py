# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyreporting(RPackage):
	"""Helps creating report for improving Reproducible Computational Research

	An S4 class for facilitating the automated creation of rmarkdown files inside other packages/software even without knowing rmarkdown language. Best if implemented in functions as "recursive" style programming.
	"""
	
	bioc = "easyreporting" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/easyreporting_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/easyreporting/easyreporting_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="918da29b5682f8956f6be279a07fe1b44f795367b023a26dca0a23b683965a78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
