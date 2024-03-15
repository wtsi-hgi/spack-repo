# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSass(RPackage):
	"""Syntactically Awesome Style Sheets ('Sass').

	An 'SCSS' compiler, powered by the 'LibSass' library. With this, R
	developers can use variables, inheritance, and functions to generate
	dynamic style sheets. The package uses the 'Sass CSS' extension language,
	which is stable, powerful, and CSS compatible."""

	cran = "sass"

	license("MIT")

	version("0.4.8", md5="1b541e8a0ce9ec67ade93869740db4b8")

	depends_on("r-fs@1.2.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
