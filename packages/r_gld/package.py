# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGld(RPackage):
	"""Estimation and Use of the Generalised (Tukey) Lambda
Distribution

	The generalised lambda distribution, or Tukey lambda distribution, 
  provides a wide variety of shapes with one functional form.   
  This package provides random numbers, quantiles, probabilities, 
  densities and density quantiles for four different types of the distribution,
  the FKML (Freimer et al 1988), RS (Ramberg and Schmeiser 1974), GPD (van Staden
  and Loots 2009) and FM5 - see documentation for details.
  It provides the density function, distribution function, and Quantile-Quantile 
  plots.  
  It implements a variety of estimation methods for the distribution, 
  including diagnostic plots. 
  Estimation methods include the starship (all 4 types), 
  method of L-Moments for the GPD and FKML types, and a 
  number of methods for only the FKML type.  
  These include maximum likelihood, maximum product of spacings, 
  Titterington's method, Moments, Trimmed L-Moments and 
  Distributional Least Absolutes. 
	"""
	
	homepage = "https://github.com/newystats/gld/"
	cran = "gld" 

	version("2.6.6", md5="8f019a846ae91a9bb278431c5d2c8d40")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
