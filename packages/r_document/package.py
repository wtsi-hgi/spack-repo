# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocument(RPackage):
	"""Run 'roxygen2' on (Chunks of) Single Code Files

	Have you ever been tempted to create 'roxygen2'-style documentation
    comments for one of your functions that was not part of one of your
    packages (yet)?
    This is exactly what this package is about: running 'roxygen2' on
    (chunks of) a single code file.
	"""
	
	homepage = "https://gitlab.com/fvafrcu/document"
	cran = "document" 

	version("4.0.0", md5="efef4c934116b30e15c4d9cb5d635da0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-fritools", type=("build", "run"))
	depends_on("r-rcmdcheck", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
