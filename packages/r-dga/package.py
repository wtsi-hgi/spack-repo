# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDga(RPackage):
	"""Capture-Recapture Estimation using Bayesian Model Averaging

	Performs Bayesian model averaging for capture-recapture. This includes code to stratify records, check the strata for suitable overlap to be used for capture-recapture, and some functions to plot the estimated population size. 
	"""
	
	cran = "dga" 

	version("2.0.1", md5="e07efa9e4db1e67644a5dcb5678e1586")

	depends_on("r-chron", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
