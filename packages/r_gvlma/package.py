# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGvlma(RPackage):
	"""Global Validation of Linear Models Assumptions

	Methods from the paper: Pena, EA and Slate, EH, "Global Validation of Linear Model Assumptions," J. American Statistical Association, 101(473):341-354, 2006.
	"""
	
	cran = "gvlma" 

	version("1.0.0.3", md5="5d5de9e788d31f2a035ab04aefeb5f8f")

	depends_on("r@2.1.1:", type=("build", "run"))
