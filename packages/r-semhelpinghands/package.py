# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemhelpinghands(RPackage):
	"""Helper Functions for Structural Equation Modeling

	An assortment of helper functions for doing structural equation
  modeling, mainly by 'lavaan' for now. Most of them are time-saving functions
  for common tasks in doing structural equation modeling and reading the
  output. This package is not for functions that implement advanced statistical
  procedures. It is a light-weight package for simple functions that do simple
  tasks conveniently, with as few dependencies as possible.
	"""
	
	homepage = "https://sfcheung.github.io/semhelpinghands/"
	cran = "semhelpinghands" 

	version("0.1.9", md5="50c79e7265b350556236bb7b86dc885f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
