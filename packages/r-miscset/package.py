# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiscset(RPackage):
	"""Miscellaneous Tools Set

	A collection of miscellaneous methods to simplify various tasks,
  including plotting, data.frame and matrix transformations, environment
  functions, regular expression methods, and string and logical operations, as
  well as numerical and statistical tools. Most of the methods are simple but
  useful wrappers of common base R functions, which extend S3 generics or
  provide default values for important parameters.
	"""
	
	homepage = "https://github.com/setempler/miscset"
	cran = "miscset" 

	version("1.1.0", md5="b108c567473e476ac7f29959fbea15d4")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
