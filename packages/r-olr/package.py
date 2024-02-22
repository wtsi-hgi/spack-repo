# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlr(RPackage):
	"""Optimal Linear Regression

	The optimal linear regression olr(), runs all the possible combinations of linear regression
  equations. The olr() returns the equation which has the greatest adjusted R-squared term or the greatest R-squared term based
  on the user's discretion. Essentially, the olr() returns the best fit equation out of all the possible equations. R-squared increases 
  with the addition of an explanatory variable whether it is 'significant' or not, thus this was developed to eliminate that conundrum. 
  Adjusted R-squared is preferred to overcome this phenomenon, but each combination will still produce different results and this will
  return the best one. Complimentary functions are included which list all of the equations, all of the equations in ascending order, 
  a function to give the user a specific model's summary, and the list of adjusted R-squared terms & R-squared terms.
  A 'Python' version is available at: <https://pypi.org/project/olr/>.
	"""
	
	homepage = "https://github.com/MatHatter"
	cran = "olr" 

	version("1.1", md5="a1387237187cb28d8d59d9f0a6fc5c12")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
