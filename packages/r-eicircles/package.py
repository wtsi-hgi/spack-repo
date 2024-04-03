# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REicircles(RPackage):
	"""Ecological Inference of RxC Tables by Overdispersed-Multinomial
Models

	Estimates RxC (R by C) vote transfer matrices (ecological contingency tables) from aggregate data using the model described in Forcina et al. (2012), as extension of the model proposed in Brown and Payne (1986). Allows incorporation of covariates.
   References:
   Brown, P. and Payne, C. (1986). ''Aggregate data, ecological regression and voting transitions''. Journal of the American Statistical Association, 81, 453–460. <DOI:10.1080/01621459.1986.10478290>.
   Forcina, A., Gnaldi, M. and Bracalente, B. (2012). ''A revised Brown and Payne model of voting behaviour applied to the 2009 elections in Italy''. Statistical Methods & Applications, 21, 109–119. <DOI:10.1007/s10260-011-0184-x>.
	"""
	
	cran = "eiCircles" 

	version("0.0.1-6", md5="8db49aa6831f0d2b085fd5538a4cbf37")
	version("0.0.1-7", md5="cddfb9f9393f00cc1b4d23994d4a51cd")

	depends_on("r-nlcoptim@0.6:", type=("build", "run"))
