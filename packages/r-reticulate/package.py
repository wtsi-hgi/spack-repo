# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReticulate(RPackage):
	"""Interface to 'Python'.

	Interface to 'Python' modules, classes, and functions. When calling into
	'Python', R data types are automatically converted to their equivalent
	'Python' types. When values are returned from 'Python' to R they are
	converted back to R types. Compatible with all versions of 'Python' >=
	2.7."""

	cran = "reticulate"

	version("1.34.0", md5="109bbcb55d3a8e779babe90e432c172a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpptoml", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("python@2.7:", type=("build", "link", "run"))
