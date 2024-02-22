# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdroc(RPackage):
	"""Nonparametric Estimation of Time-Dependent ROC, Brier Score, and
Survival Difference from Right Censored Time-to-Event Data with
or without Competing Risks

	The tdROC package facilitates the estimation of time-dependent ROC 
    (Receiver Operating Characteristic) curves and the Area Under the time-dependent 
    ROC Curve (AUC) in the context of survival data, accommodating scenarios with 
    right censored data and the option to account for competing risks. In addition 
    to the ROC/AUC estimation, the package also estimates time-dependent Brier score and 
    survival difference. Confidence intervals of various estimated quantities can be 
    obtained from bootstrap. The package also offers plotting functions for visualizing 
    time-dependent ROC curves.
	"""
	
	cran = "tdROC" 

	version("2.0", md5="aae5ce135c18d54d16c53d8685918d27")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival@3.4:", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
