# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvcompare(RPackage):
	"""Compares Cox and Survival Random Forests to Quantify
Nonlinearity

	Performs repeated nested cross-validation for Cox Proportionate Hazards, Cox Lasso, Survival Random Forest, and their ensemble. Returns internally validated concordance index, time-dependent area under the curve, Brier score, calibration slope, and statistical testing of non-linear ensemble outperforming the baseline Cox model. In this, it helps researchers to quantify the gain of using a more complex survival model, or justify its redundancy. Equally, it shows the performance value of the non-linear and interaction terms, and may highlight the need of further feature transformation. Further details can be found in Shamsutdinova, Stamate, Roberts, & Stahl (2022) "Combining Cox Model and Tree-Based Algorithms to Boost Performance and Preserve Interpretability for Health Outcomes" <doi:10.1007/978-3-031-08337-2_15>, where the method is described as Ensemble 1.
	"""
	
	cran = "survcompare" 

	version("0.1.2", md5="0f42b586d60b286582c8d50a2d40daa6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-survival@3:", type=("build", "run"))
	depends_on("r-timeroc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-randomforestsrc", type=("build", "run"))
