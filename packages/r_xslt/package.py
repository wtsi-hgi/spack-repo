# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXslt(RPackage):
	"""Extensible Style-Sheet Language Transformations

	An extension for the 'xml2' package to transform XML documents
    by applying an 'xslt' style-sheet.
	"""
	
	homepage = "https://ropensci.r-universe.dev/xslt"
	cran = "xslt" 

	version("1.4.4", md5="b16f63db2792f09fca544023230ffb26")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("libxslt", type=("build", "link", "run"))
