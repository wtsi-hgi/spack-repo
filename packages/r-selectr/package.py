# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectr(RPackage):
	"""Translate CSS Selectors to XPath Expressions.

	Translates a CSS3 selector into an equivalent XPath expression. This allows
	us to use CSS selectors when working with the XML package as it can only
	evaluate XPath expressions. Also provided are convenience functions useful
	for using CSS selectors on XML nodes. This package is a port of the Python
	package 'cssselect' (<https://cssselect.readthedocs.io/>)."""

	cran = "selectr"

	version("0.4-2", md5="165e7b67a11f58c53e55fee4b0da944e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
