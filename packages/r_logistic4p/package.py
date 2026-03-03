# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogistic4p(RPackage):
	"""Logistic Regression with Misclassification in Dependent
Variables

	Error in a binary dependent variable, also known as misclassification, has not drawn much attention in psychology. Ignoring misclassification in logistic regression can result in misleading parameter estimates and statistical inference. This package conducts logistic regression analysis with misspecification in outcome variables. 
	"""
	
	cran = "logistic4p" 

	version("1.6", md5="85af30da2eed782012a5e583e73847b3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
