# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3plus(RPackage):
	"""Seamless 'D3Plus' Integration

	Provides functions that offer seamless 'D3Plus' integration. The examples provided here are taken from the official 'D3Plus' website <http://d3plus.org>.
	"""
	
	cran = "d3plus" 

	version("0.1.0", md5="c18b7bb4caf8a864c9966e5f4803ba9b")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
