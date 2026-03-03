# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmBeta(RPackage):
	"""Add Standardized Regression Coefficients to Linear-Model-Objects

	Adds standardized regression coefficients to objects created by 'lm'. Also extends the S3 methods 'print', 'summary' and 'coef' with additional boolean argument 'standardized' and provides 'xtable'-support.
	"""
	
	cran = "lm.beta" 

	version("1.7-2", md5="2d8865e7d84b54ed272074e84ac310f9")

	depends_on("r-xtable", type=("build", "run"))
