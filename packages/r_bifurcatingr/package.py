# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBifurcatingr(RPackage):
	"""Bifurcating Autoregressive Models

	Estimation of bifurcating autoregressive models of any order, p, BAR(p) as well as several types of bias correction for the least squares estimators of the autoregressive parameters as described in Zhou and Basawa (2005) <doi:10.1016/j.spl.2005.04.024> and Elbayoumi and Mostafa (2020) <doi:10.1002/sta4.342>. Currently, the bias correction methods supported include bootstrap (single, double and fast-double) bias correction and linear-bias-function-based bias correction. Functions for generating and plotting bifurcating autoregressive data from any BAR(p) model are also included. This new version includes calculating several type of bias-corrected and -uncorrected confidence intervals for the least squares estimators of the autoregressive parameters as described in Elbayoumi and Mostafa (2023)
             <doi:10.6339/23-JDS1092>.
	"""
	
	cran = "bifurcatingr" 

	version("2.0.0", md5="ff1387474deee41697ba3c5eda6ad01f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fmultivar@4021.83:", type=("build", "run"))
