# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoodpractice(RPackage):
	"""Advice on R Package Building

	Give advice about good practices when building R packages.
    Advice includes functions and syntax to avoid, package structure, code
    complexity, code formatting, etc.
	"""
	
	homepage = "https://github.com/mangothecat/goodpractice"
	cran = "goodpractice" 

	version("1.0.4", md5="eb16910769f2d9f0440bd50fad2f420e")

	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-covr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cyclocomp@1.1:", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lintr@3:", type=("build", "run"))
	depends_on("r-praise", type=("build", "run"))
	depends_on("r-rcmdcheck", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-xmlparsedata@1.0.1:", type=("build", "run"))
