# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparktex(RPackage):
	"""Generate LaTeX sparklines in R

	Generate syntax for use with the sparklines package for
        LaTeX.
	"""
	
	homepage = "http://thomasleeper.com/software.html"
	cran = "sparktex" 

	version("0.1", md5="371eda15897562c6e522b16cd63171cc")

	depends_on("r@3:", type=("build", "run"))
