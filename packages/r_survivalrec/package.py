# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvivalrec(RPackage):
	"""Nonparametric Estimation of the Distribution of Gap Times for
Recurrent Events

	Provides estimates for the bivariate and trivariate distribution 
             functions and bivariate and trivariate survival functions for 
             censored gap times. Two approaches, using existing methodologies, 
             are considered: (i) the Lin's estimator, which is based on the 
             extension the Kaplan-Meier estimator of the distribution function 
             for the first event time and the Inverse Probability of Censoring 
             Weights for the second time (Lin DY, Sun W, Ying Z (1999) 
             <doi:10.1093/biomet/86.1.59> and (ii) another estimator
             based on Kaplan-Meier weights (Una-Alvarez J, Meira-Machado L (2008)
             <https://w3.math.uminho.pt/~lmachado/Biometria_conference.pdf>). 
             The proposed methods are the landmark estimators based on 
             subsampling approach, and the estimator based on weighted cumulative
             hazard estimator. The package also provides nonparametric estimator
             conditional to a given continuous covariate. All these methods have
             been submitted to be published.  
	"""
	
	cran = "survivalREC" 

	version("1.1", md5="4e09adb1d7eff2dff257864cb25d4f9f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
