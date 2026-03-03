# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRd2md(RPackage):
	"""Markdown Reference Manuals

	Native R only allows PDF exports of reference manuals.
    The 'Rd2md' package converts the package documentation files into
    markdown files and combines them into a markdown version of the package
    reference manual.
	"""
	
	homepage = "https://github.com/quantsch/rd2md"
	cran = "Rd2md" 

	version("1.0.0", md5="41c6e2449feeed27dd05515b799f69c1")
	version("0.0.5", md5="21b07b26cf460352767e17759a0690d8")

	depends_on("r@3.6:", type=("build", "run"))
