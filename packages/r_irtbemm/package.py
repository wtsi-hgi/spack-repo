# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtbemm(RPackage):
	"""Family of Bayesian EMM Algorithm for Item Response Models

	Applying the family of the Bayesian Expectation-Maximization-Maximization (BEMM) algorithm to estimate: (1) Three parameter logistic (3PL) model proposed by Birnbaum (1968, ISBN:9780201043105); (2) four parameter logistic (4PL) model proposed by Barton & Lord (1981) <doi:10.1002/j.2333-8504.1981.tb01255.x>; (3) one parameter logistic guessing (1PLG) and (4) one parameter logistic ability-based guessing (1PLAG) models proposed by San Martín et al (2006) <doi:10.1177/0146621605282773>. The BEMM family includes (1) the BEMM algorithm for 3PL model proposed by Guo & Zheng (2019) <doi:10.3389/fpsyg.2019.01175>; (2) the BEMM algorithm for 1PLG model and (3) the BEMM algorithm for 1PLAG model proposed by Guo, Wu, Zheng, & Chen (2021) <doi:10.1177/0146621621990761>; (4) the BEMM algorithm for 4PL model proposed by Zheng, Guo, & Kern (2021) <doi:10.1177/21582440211052556>; and (5) their maximum likelihood estimation versions proposed by Zheng, Meng, Guo, & Liu (2018) <doi:10.3389/fpsyg.2017.02302>. Thus, both Bayesian modal estimates and maximum likelihood estimates are available.
	"""
	
	cran = "IRTBEMM" 

	version("1.0.8", md5="cdbaa4a3f68fcc3be9c460e0ba0f7496")

	depends_on("r@3.5:", type=("build", "run"))
