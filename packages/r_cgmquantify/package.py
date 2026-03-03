# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgmquantify(RPackage):
	"""Analyzing Glucose and Glucose Variability

	Continuous glucose monitoring (CGM) systems provide real-time, 
  dynamic glucose information by tracking interstitial glucose values 
  throughout the day. Glycemic variability, also known as glucose variability, 
  is an established risk factor for hypoglycemia (Kovatchev) and 
  has been shown to be a risk factor in diabetes complications. 
  Over 20 metrics of glycemic variability have been identified. 
  Here, we provide functions to calculate glucose summary metrics, 
  glucose variability metrics (as defined in clinical publications), 
  and visualizations to visualize trends in CGM data.
  Cho P, Bent B, Wittmann A, et al. (2020) <https://diabetes.diabetesjournals.org/content/69/Supplement_1/73-LB.abstract>
  American Diabetes Association (2020) <https://professional.diabetes.org/diapro/glucose_calc>
  Kovatchev B (2019) <doi:10.1177/1932296819826111>
  Kovdeatchev BP (2017) <doi:10.1038/nrendo.2017.3>
  Tamborlane W V., Beck RW, Bode BW, et al. (2008) <doi:10.1056/NEJMoa0805017>
  Umpierrez GE, P. Kovatchev B (2018) <doi:10.1016/j.amjms.2018.09.010>.
	"""
	
	cran = "cgmquantify" 

	version("0.1.0", md5="d7168bfb0a7bfaa978915715c2ace55d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
