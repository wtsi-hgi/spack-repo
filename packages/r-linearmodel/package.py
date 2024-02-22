# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinearmodel(RPackage):
	"""Linear Model Functions

	Functions to access and test results from a linear model. 
	"""
	
	cran = "linearModel" 

	version("1.0.2", md5="78ae86af3c500ef4ba60dd87da810592")

	depends_on("r@3.6:", type=("build", "run"))
