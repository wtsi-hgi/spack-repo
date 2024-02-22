# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThisPath(RPackage):
	"""Get Executing Script's Path

	Determine the path of the executing script. Compatible
        with a few popular GUIs: 'Rgui', 'RStudio', 'VSCode',
        'Jupyter', 'Emacs', and 'Rscript' (shell). Compatible with
        several functions and packages: 'source()', 'sys.source()',
        'debugSource()' in 'RStudio', 'compiler::loadcmp()',
        'utils::Sweave()', 'box::use()', 'knitr::knit()',
        'plumber::plumb()', 'shiny::runApp()', 'package:targets', and
        'testthat::source_file()'.
	"""
	
	homepage = "https://github.com/ArcadeAntics/this.path"
	cran = "this.path" 

	version("2.4.0", md5="6a2c32b15f15ba4fc0302865b20799fd")

	depends_on("r@2.15:", type=("build", "run"))
