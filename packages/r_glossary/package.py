# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlossary(RPackage):
	"""Glossaries for Markdown and Quarto Documents

	Add glossaries to markdown and quarto documents by tagging individual words. Definitions can be provided inline or in a separate file.
	"""
	
	homepage = "https://github.com/debruine/glossary"
	cran = "glossary" 

	version("1.0.0", md5="5904073928caa1bdc5b2c9fc89720af0")

	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
