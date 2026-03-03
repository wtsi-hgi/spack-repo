# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPylintr(RPackage):
	"""Lint 'Python' Files with a R Command or a 'RStudio' Addin

	Allow to run 'pylint' on Python files with a R command or a 'RStudio' addin. The report appears in the RStudio viewer pane as a formatted HTML file.
	"""
	
	homepage = "https://github.com/stla/pylintR"
	cran = "pylintR" 

	version("0.1.0", md5="d33ee53235835cec67e0cad685ad09c2")

	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("py-pylint", type=("build", "link", "run"))
