# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogicdt(RPackage):
	"""Identifying Interactions Between Binary Predictors

	A statistical learning method that tries to find the best set
  of predictors and interactions between predictors for modeling binary or
  quantitative response data in a decision tree. Several search algorithms
  and ensembling techniques are implemented allowing for finetuning the
  method to the specific problem. Interactions with quantitative
  covariables can be properly taken into account by fitting local
  regression models. Moreover, a variable importance measure for assessing
  marginal and interaction effects is provided. Implements the
  procedures proposed by Lau et al. (2024, <doi:10.1007/s10994-023-06488-6>).
	"""
	
	cran = "logicDT" 

	version("1.0.4", md5="a746e8098a074293999d90919cafb235")

	depends_on("r-glmnet", type=("build", "run"))
