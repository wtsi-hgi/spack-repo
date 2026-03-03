# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibratr(RPackage):
	"""Mapping ML Scores to Calibrated Predictions

	Transforms your uncalibrated Machine Learning scores to well-calibrated prediction estimates that can be interpreted as probability estimates. The implemented BBQ (Bayes Binning in Quantiles) model is taken from Naeini (2015, ISBN:0-262-51129-0). Please cite this paper: Schwarz J and Heider D, Bioinformatics 2019, 35(14):2458-2465.
	"""
	
	cran = "CalibratR" 

	version("0.1.2", md5="c66d1d7301323fcebd4e2a390c29c748")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
