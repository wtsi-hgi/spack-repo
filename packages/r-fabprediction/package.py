# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabprediction(RPackage):
	"""Compute FAB (Frequentist and Bayes) Conformal Prediction
Intervals

	Computes and plots prediction intervals for numerical 
  data or prediction sets for categorical data using prior information. 
  Empirical Bayes procedures to estimate the prior information from 
  multi-group data are included. See, e.g.,Bersson and Hoff (2022) 
  <arXiv:2204.08122> "Optimal Conformal Prediction for Small Areas". 
	"""
	
	homepage = "https://github.com/betsybersson/fabPrediction"
	cran = "fabPrediction" 

	version("1.0.4", md5="29acef48090c809b2f74b8662f056ef6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sae@1.3:", type=("build", "run"))
