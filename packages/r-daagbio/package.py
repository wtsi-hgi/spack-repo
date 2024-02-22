# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaagbio(RPackage):
	"""Data Sets and Functions, for Demonstrations with Expression
Arrays and Gene Sequences

	Data sets and functions, for the display of gene expression array (microarray) data, and for demonstrations with such data.
	"""
	
	homepage = "https://github.com/jhmaindonald/DAAGbio/"
	cran = "DAAGbio" 

	version("0.63-4", md5="ed6652bea64a5bec3af48461f2a8f079")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-limma@2.9.15:", type=("build", "run"))
