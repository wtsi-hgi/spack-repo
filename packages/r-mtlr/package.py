# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtlr(RPackage):
	"""Survival Prediction with Multi-Task Logistic Regression

	An implementation of Multi-Task Logistic Regression (MTLR) for R. 
  This package is based on the method proposed by Yu et al. (2011) which utilized MTLR for generating individual survival curves
  by learning feature weights which vary across time. This model was further extended to account for left and interval censored data.
	"""
	
	homepage = "https://github.com/haiderstats/MTLR"
	cran = "MTLR" 

	version("0.2.1", md5="eac5c0b0422b80cc4abfee7f3d5a3f21")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival@2.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
