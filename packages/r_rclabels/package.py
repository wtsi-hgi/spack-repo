# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRclabels(RPackage):
	"""Manipulate Matrix Row and Column Labels with Ease

	Functions to assist manipulation of matrix 
             row and column labels for all types of matrix mathematics
             where row and column labels are to be respected.
	"""
	
	homepage = "https://matthewheun.github.io/RCLabels/"
	cran = "RCLabels" 

	version("0.1.10", md5="352277dde61a2ee0aa8d8825955c46d6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
