# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfino(RPackage):
	"""Kalman Filter for Impulse Noised Outliers

	A method for detecting outliers with a Kalman filter on impulsed 
  noised outliers and prediction on cleaned data. 'kfino' is a robust 
  sequential algorithm allowing to filter data with a large number of outliers. 
  This algorithm is based on simple latent linear Gaussian processes as in the 
  Kalman Filter method and is devoted to detect impulse-noised outliers. These 
  are data points that differ significantly from other observations. 'ML' 
  (Maximization Likelihood) and 'EM' (Expectation-Maximization algorithm) 
  algorithms were implemented in 'kfino'. The method is described in full 
  details in the following arXiv e-Print: <arXiv:2208.00961>.
	"""
	
	homepage = "https://forgemia.inra.fr/isabelle.sanchez/kfino"
	cran = "kfino" 

	version("1.0.0", md5="45fcb755ceadaaf8e47c35004f12e9b0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
