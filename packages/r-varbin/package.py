# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarbin(RPackage):
	"""Optimal Binning of Continuous and Categorical Variables

	Tool for easy and efficient discretization of continuous and categorical data. 
    The package calculates the most optimal binning of a given explanatory variable with respect to a 
    user-specified target variable. The purpose is to assign a unique Weight-of-Evidence value 
    to each of the calculated binpoints in order to recode the original variable. 
    The package allows users to impose certain restrictions on the functional form on the resulting 
    binning while maximizing the overall information value in the original data. 
    The package is well suited for logistic scoring models where input variables may be subject to 
    restrictions such as linearity by e.g. regulatory authorities. An excellent source describing in 
    detail the development of scorecards, and the role of Weight-of-Evidence coding in credit scoring 
    is (Siddiqi 2006, ISBN: 978–0-471–75451–0). The package utilizes the discrete nature of decision trees and 
    Isotonic Regression to accommodate the trade-off between flexible functional forms and maximum 
    information value.
	"""
	
	cran = "varbin" 

	version("0.2.1", md5="d17d8f17c479bc1ba17a590604483caa")

	depends_on("r-rpart", type=("build", "run"))
