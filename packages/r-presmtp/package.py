# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresmtp(RPackage):
	"""Methods for Transition Probabilities

	Provides a function for estimating the transition probabilities in an illness-death model. 
            The transition probabilities can be estimated from the unsmoothed landmark estimators developed 
            by de Una-Alvarez and Meira-Machado (2015) <doi:10.1111/biom.12288>.
            Presmoothed estimates can also be obtained through the use of a parametric family of binary
            regression curves, such as logit, probit or cauchit. The additive logistic regression model 
            and nonparametric regression are also alternatives which have been implemented.
            The idea behind the presmoothed landmark estimators is to use the presmoothing techniques 
            developed by  Cao et al. (2005) <doi:10.1007/s00180-007-0076-6> in the 
            landmark estimation of the transition probabilities.
	"""
	
	cran = "presmTP" 

	version("1.1.0", md5="6e300641f9552249a8d2f785635ab0a3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survpresmooth", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
