# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrorna(RPackage):
	"""Data and functions for dealing with microRNAs

	Different data resources for microRNAs and some functions for manipulating them.
	"""
	
	bioc = "microRNA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/microRNA_1.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/microRNA/microRNA_1.60.0.tar.gz"]

	version("1.60.0", md5="04b7af542581242a8e6ba5d4f19c14ca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biostrings@2.11.32:", type=("build", "run"))
