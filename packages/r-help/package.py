# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelp(RPackage):
	"""Tools for HELP data analysis

	The package contains a modular pipeline for analysis of HELP microarray data, and includes graphical and mathematical tools with more general applications.
	"""
	
	bioc = "HELP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HELP_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HELP/HELP_1.60.0.tar.gz"]

	version("1.60.0", sha256="3fb232600983542245885ecc5d3b5623e0ef3d28b314a16ae104e4fc6cbea560")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
