# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultisiteAccuracy(RPackage):
	"""Estimation of Accuracy in Multisite Machine-Learning Models

	The effects of the site may severely bias the accuracy of a multisite machine-learning model, even if the analysts removed them when fitting the model in the 'training set' and applying the model in the 'test set' (Solanes et al., Neuroimage 2023, 265:119800). This simple R package estimates the accuracy of a multisite machine-learning model unbiasedly, as described in (Solanes et al., Psychiatry Research: Neuroimaging 2021, 314:111313). It currently supports the estimation of sensitivity, specificity, balanced accuracy (for binary or multinomial variables), the area under the curve, correlation, mean squarer error, and hazard ratio for binomial, multinomial, gaussian, and survival (time-to-event) outcomes.
	"""
	
	cran = "multisite.accuracy" 

	version("1.2", md5="9604fb6be81a663d9a5674e7ab9391ba")

	depends_on("r-aroc", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-logistf", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
