# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWally(RPackage):
	"""The Wally Calibration Plot for Risk Prediction Models

	A prediction model is calibrated if, roughly, for any percentage x we can expect that x subjects out of 100 experience the event among all subjects that have a predicted risk of x%. A calibration plot provides a simple, yet useful, way of assessing the calibration assumption. The Wally plot consists of a sequence of usual calibration plots. Among the plots contained within the sequence, one is the actual calibration plot which has been obtained from the data and the others are obtained from similar simulated data under the calibration assumption. It provides the investigator with a direct visual understanding of the shape and sampling variability that are common under the calibration assumption. The original calibration plot from the data is included randomly among the simulated calibration plots, similarly to a police lineup. If the original calibration plot is not easily identified then the calibration assumption is not contradicted by the data. The method handles the common situations in which the data contain censored observations and occurrences of competing events.
	"""
	
	cran = "wally" 

	version("1.0.10", md5="f9b0d12dde26774b59473b06b0eb5574")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-prodlim@1.4.9:", type=("build", "run"))
	depends_on("r-riskregression@1.0.8:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
