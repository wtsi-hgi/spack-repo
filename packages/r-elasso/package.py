# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElasso(RPackage):
	"""Enhanced Least Absolute Shrinkage and Selection Operator
Regression Model

	Performs some enhanced variable selection algorithms 
  based on the least absolute shrinkage and selection operator for regression model.
	"""
	
	cran = "elasso" 

	version("1.1", md5="67c64ac34b6384e0e2dc9fac85b6da63")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-sizer", type=("build", "run"))
