# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwim(RPackage):
	"""Scenario Weights for Importance Measurement

	An efficient sensitivity analysis for stochastic models based on 
    Monte Carlo samples. Provides weights on simulated scenarios from a 
    stochastic model, such that stressed random variables fulfil given 
    probabilistic constraints (e.g. specified values for risk measures), 
    under the new scenario weights. Scenario weights are selected by 
    constrained minimisation of the relative entropy to the baseline model. 
    The 'SWIM' package is based on Pesenti S.M., Millossovich P., Tsanakas A. (2019)
    "Reverse Sensitivity Testing: What does it take to break the model" 
    <openaccess.city.ac.uk/id/eprint/18896/> and Pesenti S.M. (2021) 
    "Reverse Sensitivity Analysis for Risk Modelling" <https://www.ssrn.com/abstract=3878879>.
	"""
	
	homepage = "https://github.com/spesenti/SWIM"
	cran = "SWIM" 

	version("1.0.0", md5="60b55d60ff42a213c73e7eba2a3f1877")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
