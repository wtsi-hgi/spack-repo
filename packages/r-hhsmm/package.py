# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHhsmm(RPackage):
	"""Hidden Hybrid Markov/Semi-Markov Model Fitting

	Develops algorithms for fitting, prediction, simulation 
  and initialization of the hidden hybrid Markov/semi-Markov model, 
  introduced by Guedon (2005) <doi:10.1016/j.csda.2004.05.033>, 
  which also includes several tools for handling missing data, 
  nonparametric mixture of B-splines emissions (Langrock et al., 2015
  <doi:10.1111/biom.12282>), fitting regime switching regression 
  (Kim et al., 2008 <doi:10.1016/j.jeconom.2007.10.002>) and auto-regressive 
  hidden hybrid Markov/semi-Markov model, spline-based nonparametric 
  estimation of additive state-switching models  
  (Langrock et al., 2018 <doi:10.1111/stan.12133>)
  and many other useful tools 
  (read for more description: Amini et al., 2022 <doi:10.1007/s00180-022-01248-x> and its 
  arxiv version: <arXiv:2109.12489>). 
	"""
	
	cran = "hhsmm" 

	version("0.3.6", md5="3e21b00e4ca2c5c86c779a95936ab088")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cmapss", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
