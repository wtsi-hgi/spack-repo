# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShiny(RPackage):
	"""Web Application Framework for R.

	Makes it incredibly easy to build interactive web applications with R.
	Automatic "reactive" binding between inputs and outputs and extensive
	pre-built widgets make it possible to build beautiful, responsive, and
	powerful applications with minimal effort."""

	cran = "shiny"

	license("GPL-3.0-only OR custom")

	version("1.8.0", md5="cde8fa9cf462ecf2aabb7947826eea52")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-httpuv@1.5.2:", type=("build", "run"))
	depends_on("r-mime@0.3:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-fontawesome@0.4:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-sourcetools", type=("build", "run"))
	depends_on("r-later@1:", type=("build", "run"))
	depends_on("r-promises@1.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-fastmap@1.1.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-commonmark@1.7:", type=("build", "run"))
	depends_on("r-glue@1.3.2:", type=("build", "run"))
	depends_on("r-bslib@0.3:", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
