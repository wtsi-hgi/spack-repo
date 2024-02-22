# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRd2md(RPackage):
	"""Markdown Reference Manuals

	The native R functionalities only allow PDF exports of reference manuals. This shall be extended by converting the package documentation files into markdown files and combining them into a markdown version of the package reference manual.
	"""
	
	cran = "Rd2md" 

	version("0.0.5", md5="21b07b26cf460352767e17759a0690d8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
