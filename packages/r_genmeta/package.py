# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenmeta(RPackage):
	"""Implements Generalized Meta-Analysis Using Iterated Reweighted
Least Squares Algorithm

	Generalized meta-analysis is a technique for estimating parameters associated with a multiple regression model through meta-analysis of studies which may have information only on partial sets of the regressors. It estimates the effects of each variable while fully adjusting for all other variables that are measured in at least one of the studies. Using algebraic relationships between regression parameters in different dimensions, a set of moment equations is specified for estimating the parameters of a maximal model through information available on sets of parameter estimates from a series of reduced models available from the different studies. The specification of the equations requires a reference dataset to estimate the joint distribution of the covariates. These equations are solved using the generalized method of moments approach, with the optimal weighting of the equations taking into account uncertainty associated with estimates of the parameters of the reduced models. The proposed framework is implemented using iterated reweighted least squares algorithm for fitting generalized linear regression models. For more details about the method, please see pre-print version of the manuscript on generalized meta-analysis by Prosenjit Kundu, Runlong Tang and Nilanjan Chatterjee (2018) <doi:10.1093/biomet/asz030>.The current version (0.2.0) is updated to address some of the stability issues in the previous version (0.1).
	"""
	
	cran = "GENMETA" 

	version("0.2.0", md5="a4029ede8291bb59f8b2b80ebf12aefa")

	depends_on("r@2.15.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
