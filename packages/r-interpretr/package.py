# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterpretr(RPackage):
	"""Binary Classifier and Regression Model Interpretation Functions

	Compute permutation- based performance measures and create partial
    dependence plots for (cross-validated) 'randomForest' and 'ada' models.
	"""
	
	cran = "interpretR" 

	version("0.2.5", md5="c50b7a7dc730ec6bf6dce60c223eac91")

	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-auc", type=("build", "run"))
