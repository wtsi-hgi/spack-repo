# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetdee2(RPackage):
	"""Programmatic access to the DEE2 RNA expression dataset

	Digital Expression Explorer 2 (or DEE2 for short) is a repository of processed RNA-seq data in the form of counts. It was designed so that researchers could undertake re-analysis and meta-analysis of published RNA-seq studies quickly and easily. As of April 2020, over 1 million SRA datasets have been processed. This package provides an R interface to access these expression data. More information about the DEE2 project can be found at the project homepage (http://dee2.io) and main publication (https://doi.org/10.1093/gigascience/giz022).
	"""
	
	homepage = "https://github.com/markziemann/getDEE2"
	bioc = "getDEE2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/getDEE2_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/getDEE2/getDEE2_1.12.0.tar.gz"]

	version("1.12.0", md5="5bae73105adbd3fba6517601379594c0", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/getDEE2_1.12.0.tar.gz")
	version("1.12.0", md5="5bae73105adbd3fba6517601379594c0", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/getDEE2_1.12.0.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-htm2txt", type=("build", "run"))
