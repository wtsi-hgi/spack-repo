# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROverdisp(RPackage):
	"""Overdispersion in Count Data Multiple Regression Analysis

	Detection of overdispersion in count data for multiple regression analysis.
    Log-linear count data regression is one of the most popular techniques for predictive 
    modeling where there is a non-negative discrete quantitative dependent variable. In 
    order to ensure the inferences from the use of count data models are appropriate, 
    researchers may choose between the estimation of a Poisson model and a negative binomial
    model, and the correct decision for prediction from a count data estimation is directly
    linked to the existence of overdispersion of the dependent variable, conditional to the 
    explanatory variables. Based on the studies of Cameron and Trivedi (1990)
    <doi:10.1016/0304-4076(90)90014-K> and Cameron and Trivedi (2013, ISBN:978-1107667273), 
    the overdisp() command is a contribution to researchers, providing a fast and secure 
    solution for the detection of overdispersion in count data. Another advantage is that 
    the installation of other packages is unnecessary, since the command runs in the basic 
    R language.
	"""
	
	cran = "overdisp" 

	version("0.1.2", md5="7ea93f42bfb511caed7dcb60e694991c")

