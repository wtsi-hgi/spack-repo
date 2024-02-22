# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThaipdf(RPackage):
	"""R Markdown to PDF in Thai Language

	Provide R Markdown templates and LaTeX preamble
    which are necessary for creating PDF from R Markdown documents in Thai language.
	"""
	
	homepage = "https://lightbridge-ks.github.io/thaipdf/"
	cran = "thaipdf" 

	version("0.1.2", md5="fb5781cab6a58795c4c8cb050f1c25b6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
