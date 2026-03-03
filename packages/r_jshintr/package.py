# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJshintr(RPackage):
	"""Lint 'JavaScript' Files

	Allow to run 'jshint' on 'JavaScript' files with a 'R'
    command or a 'RStudio' addin. The report appears in the 'RStudio'
    viewer pane.
	"""
	
	homepage = "https://github.com/stla/jshintr"
	cran = "jshintr" 

	version("0.1.0", md5="fdedf8f2d9801d62e61cef3beac44665")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
