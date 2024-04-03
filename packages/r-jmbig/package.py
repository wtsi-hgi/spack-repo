# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmbig(RPackage):
	"""Joint Longitudinal and Survival Model for Big Data

	Provides analysis tools for big data where the sample size is very large. It offers
             a suite of functions for fitting and predicting joint models, which allow for the simultaneous
             analysis of longitudinal and time-to-event data. This statistical methodology is particularly 
             useful in medical research where there is often interest in understanding the relationship 
             between a longitudinal biomarker and a clinical outcome, such as survival or disease progression.
             This can be particularly useful in a clinical setting where it is important to be able to predict 
             how a patient's health status may change over time. Overall, this package provides a 
             comprehensive set of tools for joint modeling of BIG data obtained as survival and 
             longitudinal outcomes with both Bayesian and non-Bayesian approaches. Its versatility
             and flexibility make it a valuable resource for researchers in many different fields,
             particularly in the medical and health sciences.  
	"""
	
	cran = "jmBIG" 

	version("0.1.2", md5="7a0ca12d7095f4cf554bbfb473054049")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jmbayes2", type=("build", "run"))
	depends_on("r-joinerml", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-fastjm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
