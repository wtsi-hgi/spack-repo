# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabulate(RPackage):
	"""Pretty Console Output for Tables

	Generates pretty console output for tables allowing for full customization
  of cell colors, font type, borders and many others attributes. It also supports 'multibyte'
  characters and nested tables.
	"""
	
	homepage = "https://github.com/mlverse/tabulate"
	cran = "tabulate" 

	version("0.1.0", md5="7ff1cffed1694033acf5baa12473c531")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
