# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnp(RPackage):
	"""Fitting the Multinomial Probit Model

	Fits the Bayesian multinomial probit model via Markov chain
 Monte Carlo.  The multinomial probit model is often used to analyze 
 the discrete choices made by individuals recorded in survey data. 
 Examples where the multinomial probit model may be useful include the 
 analysis of product choice by consumers in market research and the 
 analysis of candidate or party choice by voters in electoral studies.  
 The MNP package can also fit the model with different choice sets for 
 each individual, and complete or partial individual choice orderings 
 of the available alternatives from the choice set. The estimation is
 based on the efficient marginal data augmentation algorithm that is 
 developed by Imai and van Dyk (2005). "A Bayesian Analysis of the 
 Multinomial Probit Model Using the Data Augmentation." Journal of 
 Econometrics, Vol. 124, No. 2 (February), pp. 311-334. 
 <doi:10.1016/j.jeconom.2004.02.002>  Detailed examples are given in 
 Imai and van Dyk (2005). "MNP: R Package for Fitting the Multinomial 
 Probit Model."  Journal of Statistical Software, Vol. 14, No. 3 (May), 
 pp. 1-32. <doi:10.18637/jss.v014.i03>.
	"""
	
	homepage = "https://github.com/kosukeimai/MNP"
	cran = "MNP" 

	version("3.1-4", md5="7613e5396a2a420162e9bb0959985498")

	depends_on("r@2.1:", type=("build", "run"))
