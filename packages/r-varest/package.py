# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarest(RPackage):
	"""Variance Estimation

	Error variance estimation in ultrahigh dimensional datasets with four different methods, viz. Refitted cross validation, k-fold refitted cross validation, Bootstrap-refitted cross validation, Ensemble method.
	"""
	
	cran = "varEst" 

	version("0.1.0", md5="1b4748d3313f1f654b3c6987531d4049")

	depends_on("r-sam", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-lm-beta", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
