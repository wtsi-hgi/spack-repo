# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaylorrussell(RPackage):
	"""A Taylor-Russell Function for Multiple Predictors

	The Taylor Russell model is a widely used method for assessing test validity in personnel selection tasks. The three functions in this package extend this model in a number of notable ways. TR() estimates test validity for a single selection test via the original Taylor Russell model. It extends this model by allowing users greater flexibility in argument choice. For example, users can specify any three of the four parameters (base rate, selection ratio, criterion validity, and positive predictive value) of the Taylor Russell model and estimate the remaining parameter (see the help file for examples).  The TaylorRussell() function generalizes the original Taylor Russell model to allow for multiple selection tests (predictors).  To our knowledge, this is the first generalization of the Taylor Russell model to allow for three or more selection tests (it is also the first to correctly handle models with two selection tests). TRDemo() is a 'shiny' program for illustrating the underlying logic of the Taylor Russell model. Taylor, HC and Russell, JT (1939) "The relationship of validity coefficients to the practical effectiveness of tests in selection: Discussion and tables" <doi:10.1037/h0057079>.
	"""
	
	cran = "TaylorRussell" 

	version("1.2.1", md5="7ebc4b4a5b4f824bb3bafda65d3c1cfe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
