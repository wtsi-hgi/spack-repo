# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinp(RPackage):
	"""'pinp' is not 'PNAS'

	A 'PNAS'-alike style for 'rmarkdown', derived from the
 'Proceedings of the National Academy of Sciences of the United States
 of America' ('PNAS', see <https://www.pnas.org>) 'LaTeX' style, and
 adapted for use with 'markdown' and 'pandoc'.
	"""
	
	homepage = "http://dirk.eddelbuettel.com/code/pinp.html"
	cran = "pinp" 

	version("0.0.10", md5="9812a2eb33691a0d4216eba9dc6c913f")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
