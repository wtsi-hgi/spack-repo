# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingle(RPackage):
	"""Accurate consensus sequence from nanopore reads of a gene library

	Accurate consensus sequence from nanopore reads of a DNA gene library. SINGLe corrects for systematic errors in nanopore sequencing reads of gene libraries and it retrieves true consensus sequences of variants identified by a barcode, needing only a few reads per variant. More information in preprint doi: https://doi.org/10.1101/2020.03.25.007146.
	"""
	
	bioc = "single" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/single_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/single/single_1.6.0.tar.gz"]

	version("1.6.0", sha256="fabdd3503ab53c35e34b96b569b21bf1382cfe90cbe726b8163670476d23051b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
