# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntreggof(RPackage):
	"""Integrated Regression Goodness of Fit

	Performs Goodness of Fit for regression models 
  using Integrated Regression method. Works for several 
  different fitting techniques.
	"""
	
	cran = "intRegGOF" 

	version("0.85-5", md5="2983f66134a7b061454e71d98adfb183")

	depends_on("r@2.5:", type=("build", "run"))
