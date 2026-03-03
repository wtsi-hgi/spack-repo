# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaroc(RPackage):
	"""Continuous Biomarker Evaluation with Adjustment of Covariates

	Compute covariate-adjusted specificity at controlled sensitivity level, or covariate-adjusted sensitivity at controlled specificity level, or covariate-adjust receiver operating characteristic curve, or covariate-adjusted thresholds at controlled sensitivity/specificity level. All statistics could also be computed for specific sub-populations given their covariate values. Methods are described in Ziyi Li, Yijian Huang, Datta Patil, Martin G. Sanda (2021+) "Covariate adjustment in continuous biomarker assessment".
	"""
	
	cran = "caROC" 

	version("0.1.5", md5="bbee733141c986c64f5b61b5539a42be")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
