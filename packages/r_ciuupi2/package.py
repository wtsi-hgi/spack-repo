# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiuupi2(RPackage):
	"""Kabaila and Giri (2009) Confidence Interval

	
    Computes a confidence interval for a specified linear combination of 
    the regression parameters in a linear regression model with iid normal 
    errors with unknown variance when there is uncertain prior information 
    that a distinct specified linear combination of the regression 
    parameters takes a specified number. This confidence interval, found by 
    numerical nonlinear constrained optimization, has the required minimum coverage 
    and utilizes this uncertain prior information through desirable 
    expected length properties. This confidence interval is proposed by 
    Kabaila, P. and Giri, K. (2009) <doi:10.1016/j.jspi.2009.03.018>.
	"""
	
	cran = "ciuupi2" 

	version("1.0.1", md5="748f6c240c04e1f07bed4da0d242f94b", url="https://cran.r-project.org/src/contrib/ciuupi2_1.0.1.tar.gz")

	depends_on("r-functional", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-precisesums", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
