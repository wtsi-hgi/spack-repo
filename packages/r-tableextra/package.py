# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTableextra(RPackage):
	"""Draws an Awesome Table

	An easy-to-use tool for drawing paper-quality tables with double-information encoded in grobs shapes and colors.
	"""
	
	cran = "tableExtra" 

	version("1.0.1", md5="1dcbbf10d5832c585a4ecd0138410239")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
