# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpp(RPackage):
	"""Gaussian Process Projection

	Estimates a counterfactual using Gaussian process projection. It takes a dataframe, creates missingness in the desired outcome variable and estimates counterfactual values based on all information in the dataframe. The package writes Stan code, checks it for convergence and adds artificial noise to prevent overfitting and returns a plot of actual values and estimated counterfactual values using r-base plot.  
	"""
	
	cran = "GPP" 

	version("0.1", md5="a1397046cc282c8f36f95aa09bb7e458")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
