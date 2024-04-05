# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooledcohort(RPackage):
	"""Predicted Risk for CVD using Pooled Cohort Equations, PREVENT
Equations, and Other Contemporary CVD Risk Calculators

	The 2017 American College of Cardiology and American Heart
  Association blood pressure guideline recommends using 10-year predicted 
  atherosclerotic cardiovascular disease risk to guide the decision to 
  initiate or intensify antihypertensive medication. The guideline recommends 
  using the Pooled Cohort risk prediction equations to predict 10-year 
  atherosclerotic cardiovascular disease risk. This package implements the 
  original Pooled Cohort risk prediction equations and also incorporates 
  updated versions based on more contemporary data and statistical methods.
	"""
	
	homepage = "https://github.com/bcjaeger/PooledCohort"
	cran = "PooledCohort" 

	version("0.0.2", md5="de62d990d4f85d109f196feb3f043304")
	version("0.0.1", md5="b771e12a22bcaf1d53b4900edfa4a6dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
