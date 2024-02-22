# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinl(RPackage):
	"""'linl' is not 'Letter'

	A 'LaTeX' Letter class for 'rmarkdown', using the
 'pandoc-letter' template adapted for use with 'markdown'.
	"""
	
	homepage = "https://github.com/eddelbuettel/linl"
	cran = "linl" 

	version("0.0.5", md5="b03dc6266fa74701cd0c132c3a3ec210")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
