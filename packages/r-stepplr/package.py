# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepplr(RPackage):
	"""L2 Penalized Logistic Regression with Stepwise Variable
Selection

	L2 penalized logistic regression for both continuous and discrete predictors, with forward stagewise/forward stepwise variable selection procedure.
	"""
	
	cran = "stepPlr" 

	version("0.93", md5="fda72ede270e8be79814ff0b0dbc2193")

	depends_on("r@2:", type=("build", "run"))
