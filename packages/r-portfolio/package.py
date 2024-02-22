# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortfolio(RPackage):
	"""Analysing Equity Portfolios

	Classes for analysing and implementing equity portfolios,
    including routines for generating tradelists and calculating
    exposures to user-specified risk factors.
	"""
	
	homepage = "https://github.com/dgerlanc/portfolio"
	cran = "portfolio" 

	version("0.5-2", md5="e31425b658ab93d8d839119b37b44558")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
