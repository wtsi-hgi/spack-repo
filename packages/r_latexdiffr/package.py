# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatexdiffr(RPackage):
	"""Diff TeX, 'rmarkdown' or 'quarto' Files Using the 'latexdiff'
Utility

	Produces a PDF diff of two 'rmarkdown', 'quarto', Sweave or TeX 
  files, using the external 'latexdiff' utility.
	"""
	
	homepage = "https://github.com/hughjonesd/latexdiffr"
	cran = "latexdiffr" 

	version("0.2.0", md5="7853578a069d270b5e67c2e1f626a253")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
