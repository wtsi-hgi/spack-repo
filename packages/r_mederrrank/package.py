# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMederrrank(RPackage):
	"""Bayesian Methods for Identifying the Most Harmful Medication
Errors

	Two distinct but related statistical approaches to the problem of identifying the combinations of medication error characteristics that are more likely to result in harm are implemented in this package: 1) a Bayesian hierarchical model with optimal Bayesian ranking on the log odds of harm, and 2) an empirical Bayes model that estimates the ratio of the observed count of harm to the count that would be expected if error characteristics and harm were independent. In addition, for the Bayesian hierarchical model, the package provides functions to assess the sensitivity of results to different specifications of the random effects distributions.
	"""
	
	cran = "mederrRank" 

	version("0.1.0", md5="a18c05664730d3957f7f668609e2506b")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
