# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcharty(RPackage):
	"""Minimal R/Shiny Interface to JavaScript Library 'ECharts'

	Deliver the full functionality of 'ECharts' with minimal overhead. 'echarty' users build R lists for 'ECharts' API. Lean set of powerful commands.
	"""
	
	homepage = "https://github.com/helgasoft/echarty"
	cran = "echarty" 

	version("1.6.3", md5="f2f26cf8e17899ba3b857a5fc879c2b4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-data-tree@1:", type=("build", "run"))
