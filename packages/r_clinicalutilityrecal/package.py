# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinicalutilityrecal(RPackage):
	"""Recalibration Methods for Improved Clinical Utility of Risk
Scores

	Recalibrate risk scores (predicting binary outcomes) to improve clinical utility of risk score using weighted logistic or constrained logistic recalibration methods. Additionally, produces plots to assess the potential for recalibration to improve the clinical utility of a risk model. Methods are described in detail in Mishra, A. (2019) "Methods for Risk Markers that Incorporate Clinical Utility" <http://hdl.handle.net/1773/44068>.
	"""
	
	cran = "ClinicalUtilityRecal" 

	version("0.1.0", md5="5f0f50eebadb3e23c7deb92ecfbfd1e9")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
