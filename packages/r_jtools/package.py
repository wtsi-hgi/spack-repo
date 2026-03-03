# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJtools(RPackage):
	"""Analysis and Presentation of Social Scientific Data

	This is a collection of tools for more efficiently understanding 
  and sharing the results of (primarily) regression analyses. There are also a
  number of miscellaneous functions for statistical and programming purposes. 
  Support for models produced by the survey and lme4 packages are points of 
  emphasis.
	"""
	
	homepage = "https://jtools.jacob-long.com"
	cran = "jtools" 

	version("2.2.2", md5="006995f8f27b05cb1d6e6e3c5af9672b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
