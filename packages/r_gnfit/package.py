# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnfit(RPackage):
	"""Goodness of Fit Test for Continuous Distribution Functions

	Computes the test statistic and p-value of the Cramer-von Mises and Anderson-Darling test for some continuous distribution functions proposed by Chen and Balakrishnan (1995) <http://asq.org/qic/display-item/index.html?item=11407>. In addition to our classic distribution functions here, we  calculate the Goodness of Fit (GoF) test to dataset which follows the extreme value distribution function, without remembering the formula of distribution/density functions. Calculates the Value at Risk (VaR) and Average VaR are another important risk factors which are estimated by using well-known distribution functions. Pflug and Romisch (2007, ISBN: 9812707409) is a good reference to study the properties of risk measures.
	"""
	
	cran = "gnFit" 

	version("0.2.0", md5="6b9453eee35ef3a3826e17327006e619")

	depends_on("r-ismev", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
