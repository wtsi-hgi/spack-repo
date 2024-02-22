# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCold(RPackage):
	"""Count Longitudinal Data

	Performs regression analysis for longitudinal count data,  
   allowing for serial dependence among observations from a given 
   individual and two dimensional random effects on the linear predictor. 
   Estimation is via maximization of the exact likelihood of a suitably 
   defined model. Missing values and unbalanced data are allowed. 
   Details can be found in the accompanying scientific papers: 
   Goncalves & Cabral (2021, Journal of Statistical Software, 
   <doi:10.18637/jss.v099.i03>) and Goncalves et al. 
   (2007, Computational Statistics & Data Analysis, 
   <doi:10.1016/j.csda.2007.03.002>).
	"""
	
	cran = "cold" 

	version("2.0-3", md5="24087d53e2d1354a98d5b73ee26af272")

	depends_on("r@3.5.3:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
