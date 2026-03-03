# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLink(RPackage):
	"""Hyperlink Automatic Detection

	Automatic detection of hyperlinks for packages and calls in the text
    of 'rmarkdown' or 'quarto' documents.
	"""
	
	homepage = "https://link.tada.science/"
	cran = "link" 

	version("2024.4.0", md5="76940ad4ca9fac51906181897f9ae9c4")

	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-downlit", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
