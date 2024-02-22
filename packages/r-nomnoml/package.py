# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNomnoml(RPackage):
	"""Sassy 'UML' Diagrams

	A tool for drawing sassy 'UML' (Unified Modeling Language) diagrams 
  based on a simple syntax, see <https://www.nomnoml.com>. Supports styling, 
  R Markdown and exporting diagrams in the PNG format. Note: you need a chromium based 
  browser installed on your system.
	"""
	
	homepage = "https://rstudio.github.io/nomnoml/"
	cran = "nomnoml" 

	version("0.3.0", md5="4253432c907243925a94c0dfd2607f6d")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
