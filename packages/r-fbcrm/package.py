# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbcrm(RPackage):
	"""Phase I Optimal Dose Assignment using the FBCRM and MFBCRM
Methods

	Performs dose assignment and trial simulation for the FBCRM (Fully Bayesian Continual Reassessment Method) and MFBCRM (Mixture Fully Bayesian Continual Reassessment Method) phase I clinical trial designs. These trial designs extend the Continual Reassessment Method (CRM) and Bayesian Model Averaging Continual Reassessment Method (BMA-CRM) by allowing the prior toxicity skeleton itself to be random, with posterior distributions obtained from Markov Chain Monte Carlo. On average, the FBCRM and MFBCRM methods outperformed the CRM and BMA-CRM methods in terms of selecting an optimal dose level across thousands of randomly generated simulation scenarios. Details on the methods and results of this simulation study are available on request, and the manuscript is currently under review.
	"""
	
	cran = "FBCRM" 

	version("1.1", md5="6b1acfb3294bad42cd3ab0ed26574b7c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
