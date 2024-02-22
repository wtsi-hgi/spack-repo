# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooledcohort(RPackage):
	"""Predict 10-Year Risk for Atherosclerotic Cardiovascular Disease

	The 2017 American College of Cardiology and American Heart
  Association blood pressure guideline recommends using 10-year predicted 
  atherosclerotic cardiovascular disease risk to guide the decision to 
  initiate or intensify antihypertensive medication. The guideline recommends 
  using the Pooled Cohort risk prediction equations to predict 10-year 
  atherosclerotic cardiovascular disease risk. This package implements the 
  original Pooled Cohort risk prediction equations and also incorporates 
  updated versions based on more contemporary data and statistical methods.
  References:
  Goff DC, Lloyd-Jones DM, Bennett G, Coady S, D’Agostino RB, Gibbons R, 
  Greenland P, Lackland DT, Levy D, O’Donnell CJ, and Robinson JG (2014) 
  <doi:10.1016/j.jacc.2014.03.006>
  Yadlowsky S, Hayward RA, Sussman JB, McClelland RL, Min YI, and Basu S (2018)
  <doi:10.7326/m17-3011>.
	"""
	
	homepage = "https://github.com/bcjaeger/PooledCohort"
	cran = "PooledCohort" 

	version("0.0.1", md5="b771e12a22bcaf1d53b4900edfa4a6dd")

	depends_on("r-glue", type=("build", "run"))
