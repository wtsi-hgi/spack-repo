# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelobj(RPackage):
	"""A Model Object Framework for Regression Analysis

	A utility library to facilitate the generalization of statistical methods built on a regression framework. Package developers can use 'modelObj' methods to initiate a regression analysis without concern for the details of the regression model and the method to be used to obtain parameter estimates. The specifics of the regression step are left to the user to define when calling the function. The user of a function developed within the 'modelObj' framework creates as input a 'modelObj' that contains the model and the R methods to be used to obtain parameter estimates and to obtain predictions.  In this way, a user can easily go from linear to non-linear models within the same package.  
	"""
	
	cran = "modelObj" 

	version("4.2", md5="41362e5d5a8b4566b9f8231284ca1836")

