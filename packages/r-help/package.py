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

	version("1.60.0", md5="d7a1038ee6eb5ec01393b39e30e028fe")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
