# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNregression(RPackage):
	"""Simulation-Based Calculations of Sample Size for Linear and
Logistic Regression

	Provides a function designed to estimate the minimal sample size required to attain a specific statistical power in the context of linear regression and logistic regression models through simulations.
	"""
	
	cran = "nRegression" 

	version("0.5.1", md5="d6c493a093da32c385387177dc566f64")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-covr", type=("build", "run"))
	depends_on("r-simitation", type=("build", "run"))
